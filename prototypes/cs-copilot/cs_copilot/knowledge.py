"""FAQ knowledge base: parsing and deterministic keyword retrieval."""

import re
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

STOPWORDS = {
    "a", "an", "the", "i", "my", "me", "you", "your", "we", "our", "it", "its",
    "is", "are", "was", "be", "been", "do", "does", "did", "can", "could",
    "will", "would", "how", "what", "when", "where", "which", "who", "why",
    "to", "of", "in", "on", "for", "with", "and", "or", "not", "no", "this",
    "that", "there", "have", "has", "had", "get", "got", "please", "hi",
    "hello", "thanks", "if", "at", "by", "from", "about", "so", "just",
}


@dataclass
class FaqEntry:
    id: str
    question: str
    answer: str
    tokens: set


def tokenize(text: str) -> set:
    words = re.findall(r"[a-zäöüß]+", text.lower())
    # naive plural stemming so "returns"/"return", "products"/"product" match
    stemmed = {w[:-1] if len(w) > 3 and w.endswith("s") else w for w in words}
    return {w for w in stemmed if w not in STOPWORDS and len(w) > 2}


def load_faq(path: Path = DATA_DIR / "faq.md") -> list:
    """Parse faq.md into entries. Format: '## [id] Question' followed by the answer."""
    entries = []
    pattern = re.compile(r"^## \[([a-z-]+)\] (.+)$")
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line)
        if m:
            current = FaqEntry(id=m.group(1), question=m.group(2), answer="", tokens=set())
            entries.append(current)
        elif current is not None and line.strip():
            current.answer = (current.answer + " " + line.strip()).strip()
    for e in entries:
        e.tokens = tokenize(e.question + " " + e.answer)
    return entries


def retrieve(query: str, entries: list, top_k: int = 3) -> list:
    """Rank FAQ entries by token overlap with the query.

    Returns [(entry, score)] sorted by score desc. Score is overlap divided by
    query token count — 1.0 means every content word of the query appears in
    the entry. Deterministic: ties break on entry order in the file.
    """
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    # single shared word on a longer query is noise, not a match
    min_overlap = 2 if len(q_tokens) >= 3 else 1
    scored = []
    for e in entries:
        overlap = len(q_tokens & e.tokens)
        if overlap >= min_overlap:
            scored.append((e, overlap / len(q_tokens)))
    scored.sort(key=lambda x: -x[1])
    return scored[:top_k]
