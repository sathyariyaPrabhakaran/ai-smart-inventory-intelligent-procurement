from fastapi import FastAPI

app = FastAPI(title="AI Smart Inventory and Intelligent Procurement")

@app.get("/")
def root():
    return {
        "project": "AI-Powered Smart Inventory Management and Intelligent Procurement System Using RAG",
        "status": "Review 0 scaffold"
    }
