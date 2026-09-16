from app.services.decision_support import build_procurement_recommendation


def test_manager_approval_required():
    result = build_procurement_recommendation(100.0, [])
    assert result["manager_approval_required"] is True
