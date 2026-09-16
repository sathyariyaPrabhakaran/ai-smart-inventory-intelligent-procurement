from dataclasses import dataclass
from datetime import date

@dataclass
class DemandForecast:
    product_id: str
    forecast_date: date
    predicted_demand: float
