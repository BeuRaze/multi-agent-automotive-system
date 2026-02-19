from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import run_multi_agent_system

app = FastAPI(title="Multi-Agent Automotive API")

class CarRequest(BaseModel):
    car_name: str

@app.get("/")
def home():
    return {"message": "Multi-Agent Automotive API Running"}

@app.post("/generate-report")
def generate_report(request: CarRequest):
    result = run_multi_agent_system(request.car_name)
    return {"report": result}
