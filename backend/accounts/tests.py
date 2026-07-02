"""Tests pédagogiques pour l'app accounts.

Ces tests servent d'exemples : signup, login, logout, accès protégé, export RGPD.
Lancez : pytest accounts/
"""

import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from quizzes.models import Question, Quiz

pytestmark = pytest.mark.django_db


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(
        username="alice", email="alice@test.com", password="motdepasse123"
    )


def test_signup_creates_user(client):
    # Lot 3 : inscription par EMAIL (username = email en interne).
    response = client.post(
        "/api/accounts/signup/",
        {
            "email": "bob@test.com",
            "password": "motdepasse123",
        },
        format="json",
    )
    assert response.status_code == 201, response.data
    assert User.objects.filter(email="bob@test.com").exists()


def test_signup_requires_email(client):
    response = client.post(
        "/api/accounts/signup/",
        {"password": "motdepasse123"},
        format="json",
    )
    assert response.status_code == 400


def test_login_returns_token(client, user):
    response = client.post(
        "/api/accounts/login/",
        {"email": "alice@test.com", "password": "motdepasse123"},
        format="json",
    )
    assert response.status_code == 200, response.data
    assert "token" in response.data
    assert response.data["user"]["email"] == "alice@test.com"


def test_login_with_wrong_password(client, user):
    response = client.post(
        "/api/accounts/login/",
        {"email": "alice@test.com", "password": "wrong"},
        format="json",
    )
    assert response.status_code == 400


def test_me_requires_auth(client):
    response = client.get("/api/accounts/me/")
    assert response.status_code in (401, 403)


def test_me_with_token(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/accounts/me/")
    assert response.status_code == 200
    assert response.data["username"] == "alice"


def test_logout_invalidates_token(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.post("/api/accounts/logout/")
    assert response.status_code == 204
    # Le token n'existe plus
    assert not Token.objects.filter(key=token.key).exists()


@pytest.fixture
def authed_client(client, user):
    from rest_framework.authtoken.models import Token

    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return client


@pytest.fixture
def sample_quiz(user):
    quiz = Quiz.objects.create(
        user=user,
        title="Mon cours",
        source_text="Contenu du cours.",
        score=7,
    )
    Question.objects.create(
        quiz=quiz,
        index=1,
        prompt="Question test ?",
        options=["A", "B", "C", "D"],
        correct_index=0,
        selected_index=1,
    )
    return quiz


def test_export_requires_auth(client):
    response = client.get("/api/accounts/me/export/")
    assert response.status_code in (401, 403)


def test_export_json(authed_client, user, sample_quiz):
    response = authed_client.get("/api/accounts/me/export/")
    assert response.status_code == 200
    assert response["Content-Type"].startswith("application/json")
    assert "attachment" in response["Content-Disposition"]

    data = json.loads(response.content)
    assert data["export_version"] == "1.0"
    assert data["account"]["email"] == user.email
    assert len(data["quizzes"]) == 1
    assert data["quizzes"][0]["title"] == "Mon cours"
    assert data["quizzes"][0]["questions"][0]["selected_index"] == 1
    assert data["stats"]["total_quizzes"] == 1


def test_export_only_own_quizzes(authed_client, user, sample_quiz):
    other = User.objects.create_user(username="bob", email="bob@test.com", password="pwd12345678")
    Quiz.objects.create(user=other, title="Quiz de Bob", source_text="secret")

    response = authed_client.get("/api/accounts/me/export/")
    data = json.loads(response.content)
    assert len(data["quizzes"]) == 1
    assert data["quizzes"][0]["title"] == "Mon cours"


def test_export_empty_quizzes(authed_client, user):
    response = authed_client.get("/api/accounts/me/export/")
    data = json.loads(response.content)
    assert data["quizzes"] == []
    assert data["stats"]["total_quizzes"] == 0


def test_export_invalid_format(authed_client):
    response = authed_client.get("/api/accounts/me/export/?export_format=pdf")
    assert response.status_code == 400
