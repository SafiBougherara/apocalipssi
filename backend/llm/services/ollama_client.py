"""
Client Ollama — appel HTTP vers le service LLM LOCAL (gratuit).

[Note pédagogique] Ollama fait tourner un modèle open-source (Llama, Phi,
Mistral…) en local, sans clé API ni coût. C'est le backend par DÉFAUT du kit :
souveraineté des données + zéro coût. Sa contrepartie est la latence sur CPU
(cf. perturbation J2). Le prompt et la validation sont mutualisés dans
quiz_prompt.py et partagés avec les clients OpenAI / Claude.
"""

import logging

import requests
from django.conf import settings

from .base import LLMClient, LLMError
from .quiz_prompt import MAX_RETRIES, build_messages_prompt, parse_and_validate_quiz

logger = logging.getLogger(__name__)


class OllamaLLMClient(LLMClient):
    """Client HTTP pour Ollama — utilise /api/chat pour la séparation system/user."""

    def __init__(
        self, *, model: str | None = None, host: str | None = None, timeout: int | None = None
    ) -> None:
        self.host = (host or settings.OLLAMA_HOST).rstrip("/")
        self.model = model or settings.OLLAMA_MODEL
        self.timeout = timeout or settings.OLLAMA_TIMEOUT

    def generate_quiz(self, source_text: str, title: str) -> list[dict]:
        # Couche 2 — Séparation explicite system/user via /api/chat
        messages = build_messages_prompt(source_text, title)
        last_err: LLMError | None = None
        for attempt in range(1, MAX_RETRIES + 1):
            raw = self._call_ollama_chat(messages)
            try:
                return parse_and_validate_quiz(raw)
            except LLMError as exc:
                last_err = exc
                logger.warning(
                    "Tentative %d/%d échouée — validation : %s", attempt, MAX_RETRIES, exc
                )
        raise last_err  # type: ignore[misc]

    # ----- internals -----

    def _call_ollama_chat(self, messages: list[dict]) -> str:
        """Appel vers /api/chat (séparation system/user native)."""
        try:
            response = requests.post(
                f"{self.host}/api/chat",
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False,
                    "options": {"temperature": 0.4},
                    "format": "json",
                },
                timeout=self.timeout,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            raise LLMError(f"Ollama injoignable : {exc}") from exc

        data = response.json()
        raw = data.get("message", {}).get("content", "")
        if not raw:
            raise LLMError("Ollama a renvoyé une réponse vide.")
        return raw
