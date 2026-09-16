# System Architecture

1. Real-time inventory and historical sales provide operational data.
2. XGBoost demand forecasting estimates future product demand.
3. Festival, weather and day-of-week signals provide contextual demand information.
4. Expiry management identifies inventory requiring attention.
5. Supplier intelligence organizes price, MOQ, delivery time and previous performance information.
6. RAG retrieves relevant organization-specific documents and records.
7. An LLM combines the forecast and retrieved context into an explainable procurement recommendation.
8. A manager reviews and approves, rejects, or modifies the recommendation.
9. An approved decision can produce a purchase-order draft and tracking record.

The intended decision-support principle is: ML predicts → RAG retrieves → LLM explains/recommends → Manager approves.
