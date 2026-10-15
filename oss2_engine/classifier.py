"""Offline, deterministic issue classification. No network calls."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Classification:
    category: str
    beginner_friendly: bool


def classify_issue(title: str, labels: list[str] | None = None) -> Classification:
    if not isinstance(title, str) or not title.strip():
        raise ValueError("title must be a non-empty string")
    labels = labels or []
    if not all(isinstance(label, str) for label in labels):
        raise TypeError("labels must be strings")
    terms = f"{title} {' '.join(labels)}".casefold()
    beginner = any(term in terms for term in ("good first issue", "good-first-issue", "beginner"))
    if any(term in terms for term in ("docs", "documentation", "readme", "typo")):
        category = "documentation"
    elif any(term in terms for term in ("test", "coverage")):
        category = "testing"
    elif any(term in terms for term in ("bug", "fix", "error")):
        category = "bugfix"
    else:
        category = "other"
    return Classification(category=category, beginner_friendly=beginner)
