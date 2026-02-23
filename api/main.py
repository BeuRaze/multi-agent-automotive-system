from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.orchestrator import run_multi_agent_system

# ==============================
# CREATE FASTAPI APP
# ==============================
app = FastAPI(title="Multi-Agent Automotive API")

# ==============================
# ADD CORS MIDDLEWARE
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all domains (safe for this project)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# REQUEST MODEL
# ==============================
class CarRequest(BaseModel):
    car_name: str

# ==============================
# HEALTH CHECK ROUTE
# ==============================
@app.get("/")
def home():
    return {"message": "Multi-Agent Automotive API Running"}

# ==============================
# GENERATE REPORT ENDPOINT
# ==============================
@app.post("/generate-report")
def generate_report(request: CarRequest):
    try:
        result = run_multi_agent_system(request.car_name)
        return {"report": result}
    except Exception as e:
        return {"error": str(e)}