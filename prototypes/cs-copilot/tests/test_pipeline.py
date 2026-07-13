import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cs_copilot import knowledge, orders, rules
from cs_copilot.pipeline import run


def test_order_status_draft_is_grounded():
    result = run("What's the status of my order N-1042?")
    assert result["category"] == "order_status"
    assert not result["escalate"]
    assert "order:N-1042" in result["sources"]
    # tracking number from the order record must appear verbatim in the draft
    assert "0034129985" in result["answer_draft"]


def test_unknown_order_escalates():
    result = run("Where is my order N-9999?")
    assert result["escalate"] and result["escalation_reason"] == "order_not_found"
    assert result["answer_draft"] is None


def test_health_always_escalates_even_when_kb_could_answer():
    result = run("Does the granola contain traces of nuts? I have a nut allergy.")
    assert result["escalate"] and result["escalation_reason"] == "health_allergy"


def test_legal_escalates():
    result = run("If I don't get my money back I will contact my lawyer")
    assert result["escalate"] and result["escalation_reason"] == "legal"


def test_unrelated_question_escalates_low_confidence():
    result = run("Can you recommend a good restaurant in Berlin?")
    assert result["escalate"] and result["escalation_reason"] == "low_confidence"


def test_faq_answer_cites_source():
    result = run("When will I get my refund?")
    assert not result["escalate"]
    assert "faq:refund-timing" in result["sources"]


def test_retrieval_ranks_relevant_entry_first():
    entries = knowledge.load_faq()
    hits = knowledge.retrieve("How long does delivery take?", entries)
    assert hits and hits[0][0].id == "shipping-times"


def test_order_id_extraction():
    assert orders.extract_order_id("where is n-1042 please") == "N-1042"
    assert orders.extract_order_id("no id here") is None


def test_classify_margin_zero_when_nothing_matches():
    category, margin = rules.classify("blah blah")
    assert category == "other" and margin == 0.0
