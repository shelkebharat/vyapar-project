from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import route modules for different business domains
from app.routes import profit, analytics, churn, finance, demand, customers, inventory, notify, bot

# Initialize FastAPI application
app = FastAPI(title="Vyapaar View API")

# Configure CORS middleware to allow requests from any origin (e.g., frontend during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(profit.router)
app.include_router(analytics.router)
app.include_router(churn.router)
app.include_router(finance.router)
app.include_router(demand.router)
app.include_router(customers.router)
app.include_router(inventory.router)
app.include_router(notify.router)
app.include_router(bot.router)

@app.get("/")
def home():
    return {"message": "Vyapaar Backend Running 🚀"}