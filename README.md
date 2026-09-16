# AI-Powered Smart Inventory Management and Intelligent Procurement System Using RAG

Final Year Project – Review 0  
Batch: AIML A10  
Guide: Dr. D Prabhu  
Team: Mythili R and Sathya Priya P

## Overview
This project is an AI-powered decision-support system for retail inventory and procurement. It combines demand forecasting with organization-specific knowledge retrieval and LLM-based explanations to support procurement decisions.

### Core workflow
Real-Time Inventory → Historical Sales → XGBoost Demand Forecasting → Festival + Weather + Day Patterns → Expiry Management → Supplier Intelligence → Smart Procurement Recommendation → RAG + LLM Explanation → Manager Approval → Purchase Order & Tracking

### Key modules
- Inventory and sales management
- XGBoost demand forecasting
- Festival, weather and day-of-week context
- Expiry-aware inventory management
- Supplier intelligence
- Intelligent procurement recommendation
- RAG-based retrieval from controlled business knowledge
- LLM-generated explanations
- Manager approval / human-in-the-loop
- Purchase-order drafting and tracking

## Important scope
The project does not claim that ML, RAG, or LLMs are individually new. The focus is their integration into a unified retail procurement decision-support workflow.

**ML predicts → RAG retrieves → LLM explains/recommends → Manager approves.**

## Current status
This repository is the Review 0 foundation/scaffold. Model training, production integrations, and final evaluation are not claimed as completed yet.

## Planned stack
Python, FastAPI/Flask, SQL, pandas, NumPy, scikit-learn, XGBoost, a vector store for RAG, an LLM, and a web dashboard.

## Evaluation plan
Demand forecasting will be evaluated using suitable forecasting metrics such as MAE, RMSE and MAPE. RAG will be evaluated for retrieval relevance and groundedness. Procurement recommendations will be checked against business rules and available evidence.
