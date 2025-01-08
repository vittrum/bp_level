from fastapi import FastAPI
from db.db import Base, engine
from modules.challenge.routes import router as challenge_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(challenge_router, prefix="/api/v1", tags=["Challenges"])
