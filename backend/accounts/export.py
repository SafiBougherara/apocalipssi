"""
Export RGPD (droit à la portabilité) — agrège toutes les données d'un utilisateur.

[Note pédagogique] On centralise la logique ici plutôt que dans la vue, pour
faciliter les tests unitaires et l'ajout de nouveaux formats (JSON, ZIP, CSV).
"""

from __future__ import annotations

import csv
import io
import json
from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.utils import timezone

from quizzes.models import Quiz

from .models import get_or_create_profile

if TYPE_CHECKING:
    from django.contrib.auth.models import User

EXPORT_VERSION = "1.0"
VALID_FORMATS = frozenset({"json"})


def build_user_export(user: User) -> dict:
    """Collecte compte + profil + quiz + questions pour l'utilisateur donné."""
    profile = get_or_create_profile(user)
    quizzes = Quiz.objects.filter(user=user).prefetch_related("questions").order_by("-created_at")

    quiz_data = []
    for quiz in quizzes:
        quiz_data.append(
            {
                "id": quiz.id,
                "title": quiz.title,
                "source_text": quiz.source_text,
                "score": quiz.score,
                "created_at": quiz.created_at.isoformat(),
                "updated_at": quiz.updated_at.isoformat(),
                "questions": [
                    {
                        "index": q.index,
                        "prompt": q.prompt,
                        "options": q.options,
                        "correct_index": q.correct_index,
                        "selected_index": q.selected_index,
                    }
                    for q in quiz.questions.all()
                ],
            }
        )

    quizzes_taken = sum(1 for q in quiz_data if q["score"] is not None)

    return {
        "export_version": EXPORT_VERSION,
        "exported_at": timezone.now().isoformat(),
        "account": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "date_joined": user.date_joined.isoformat(),
            "email_verified": profile.email_verified,
            "profile_created_at": profile.created_at.isoformat(),
        },
        "quizzes": quiz_data,
        "stats": {
            "total_quizzes": len(quiz_data),
            "quizzes_taken": quizzes_taken,
        },
    }


def export_filename(user: User, ext: str) -> str:
    date = timezone.now().strftime("%Y%m%d")
    return f"edututor-export-{user.id}-{date}.{ext}"


def response_json(payload: dict, user: User) -> HttpResponse:
    content = json.dumps(payload, ensure_ascii=False, indent=2)
    response = HttpResponse(content, content_type="application/json; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{export_filename(user, "json")}"'
    return response
    """CSV tabulaire : une ligne par question (quiz répété sur chaque ligne)."""
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(
        [
            "quiz_id",
            "quiz_title",
            "quiz_score",
            "quiz_created_at",
            "question_index",
            "prompt",
            "options",
            "correct_index",
            "selected_index",
        ]
    )
    for quiz in payload["quizzes"]:
        for q in quiz["questions"]:
            writer.writerow(
                [
                    quiz["id"],
                    quiz["title"],
                    quiz["score"] if quiz["score"] is not None else "",
                    quiz["created_at"],
                    q["index"],
                    q["prompt"],
                    json.dumps(q["options"], ensure_ascii=False),
                    q["correct_index"],
                    q["selected_index"] if q["selected_index"] is not None else "",
                ]
            )
    response = HttpResponse(buf.getvalue(), content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{export_filename(user, "csv")}"'
    return response
