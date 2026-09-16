def build_procurement_recommendation(forecast: float, business_context: list[str]) -> dict:
    """Build a recommendation placeholder; manager approval remains required."""
    return {
        "forecast_demand": forecast,
        "business_context": business_context,
        "recommendation": None,
        "manager_approval_required": True,
    }
