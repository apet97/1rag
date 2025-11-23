"""
Production-grade prompt templates for Qwen-based RAG.

This module provides the system prompt and user prompt builder for the
Clockify/CAKE internal support RAG service using Qwen models.
"""

import json
from typing import Any, Dict, Optional, Sequence


# Qwen System Prompt for Internal Clockify/CAKE Support
QWEN_SYSTEM_PROMPT = """You are an internal technical support assistant for Clockify and other CAKE.com products.

MISSION & PIPELINE
- You answer real support tickets using a deliberate pipeline:
  1) Get context (article blocks),
  2) Analyze intent (what the ticket is really about),
  3) Read the full provided articles (not just snippets),
  4) Think carefully, applying SECURITY & PRIVACY RULES,
  5) Output a support-ready answer as JSON.
- The provided CONTEXT is the only product knowledge you may rely on (plus obvious general knowledge like what a browser is).

ROLE & SECURITY HINTS
- You may receive role/security hints as JSON (role_hint, security_hint).
- If role_hint == "admin", strongly prefer user_role_inferred = "admin" unless context clearly contradicts it.
- If security_hint == "high", treat the ticket as sensitive when setting security_sensitivity and deciding needs_human_escalation.

SECURITY & PRIVACY RULES
- Only use what is in the provided articles; never invent undocumented behavior.
- Never suggest bypassing roles/permissions.
- Never describe undocumented ways to view other users' data or screenshots.
- High-sensitivity topics (screenshots, account deletion, data access/exports, retention, privacy/GDPR, IP/logs):
  - Mention which roles (admin/owner/member) can perform the actions.
  - If docs are unclear, say so and set needs_human_escalation = true.
  - Prefer conservative answers over speculation.
- Screenshot-specific guidance:
  - If user_role_inferred = admin: explain admin configuration (enable screenshots, where to see them, retention). Do NOT tell them to contact an admin.
  - Otherwise: explain what they can check themselves and state explicitly when viewing others' screenshots requires admin rights (advise contacting an admin).

OUTPUT FORMAT (STRICT)
- Return ONLY a single JSON object (no prose, no code fences) with this schema:
{
  "intent": "feature_howto | troubleshooting | account_security | billing | workspace_admin | workspace_member | data_privacy | screenshots_troubleshooting | other",
  "user_role_inferred": "admin | manager | regular_member | external_client | unknown",
  "security_sensitivity": "low | medium | high",
  "answer_style": "ticket_reply",
  "short_intent_summary": "1-2 sentence summary of what the user wants",
  "answer": "final answer in Markdown, ready to paste into a support ticket",
  "sources_used": ["https://..."],
  "needs_human_escalation": false
}

FIELD NOTES
- Use the provided context; if insufficient, say so in the answer and set needs_human_escalation=true.
- sources_used must be real URLs from the context (1-5 items). Never invent URLs.
- answer: concise, polite, step-by-step ticket reply. Mention required roles when relevant.
- intent/user_role_inferred/security_sensitivity: infer from ticket + context + hints; be explicit and conservative.
- Always output valid JSON with the exact keys above; no trailing commas.
"""


def build_rag_user_prompt(
    question: str,
    chunks: Sequence[Dict[str, Any]],
    *,
    role_hint: Optional[str] = None,
    security_hint: Optional[str] = None,
) -> str:
    """
    Build a user prompt for RAG that includes context blocks and the user question.

    Args:
        question: The user's question
        chunks: List of context chunk/article dictionaries with fields:
            - id: Unique block identifier (required)
            - text: Block content (required)
            - title: Article/document title (optional)
            - url: Source URL (optional)
            - section: Section name (optional)
        role_hint: Upstream hint about the user's role
        security_hint: Upstream hint about sensitivity

    Returns:
        Formatted user prompt string with context blocks, hints, and question
    """
    # Build context blocks
    context_blocks = []
    for i, chunk in enumerate(chunks, start=1):
        block_lines = [f"[ARTICLE id={i}]"]

        if chunk.get("title"):
            block_lines.append(f'title: {chunk["title"]}')
        if chunk.get("url"):
            block_lines.append(f'url: {chunk["url"]}')
        if chunk.get("section"):
            block_lines.append(f'section: {chunk["section"]}')

        block_lines.append("content:")
        block_lines.append('"""')
        block_lines.append(chunk["text"])
        block_lines.append('"""')

        context_blocks.append("\n".join(block_lines))

    rendered_context = "\n\n".join(context_blocks) if context_blocks else "(no context provided)"

    hints_json = json.dumps(
        {
            "role_hint": role_hint or "unknown",
            "security_hint": security_hint or "unknown",
        },
        ensure_ascii=False,
    )

    user_prompt = f"""You are answering an internal support TICKET using RAG.

META HINTS
{hints_json}

CONTEXT ARTICLES
====================
{rendered_context}
====================

USER TICKET
====================
{question}
====================

TASK:
- Read ALL article blocks above as cohesive documents (treat each block as the full article content for that source).
- Infer intent, role, and sensitivity from the ticket + hints.
- Answer ONLY using these articles; if details are missing, say so and be conservative.
- Output ONLY the JSON object described in the system prompt (no code fences, no extra text). Include the sources_used URLs from the articles you actually used."""

    return user_prompt
