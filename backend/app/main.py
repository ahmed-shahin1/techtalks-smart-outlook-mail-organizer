# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← ADD THIS LINE
from app.api import routes
from app.config import settings

# Create FastAPI app
app = FastAPI(
    title="Outlook Organizer Backend",
    description="API for summarizing, categorizing, and prioritizing Outlook emails",
    version="1.0.0",
)

# ← ADD THIS ENTIRE SECTION - CRITICAL FOR OUTLOOK ADD-IN
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include API routes
app.include_router(routes.router, prefix="/api")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Outlook Organizer Backend!"}


# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )