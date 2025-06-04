from fastapi import FastAPI
from app.core.config import settings # Assuming settings are used for project name, etc.
from app.apis.v1.api import api_v1_router # Import the v1 router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/health", tags=["Public"]) # Add a tag for better organization
async def health_check():
    return {"status": "ok"}

# Include the V1 router
app.include_router(api_v1_router, prefix=settings.API_V1_STR)

# Potentially add other middleware, exception handlers etc. here
