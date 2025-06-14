from fastapi import FastAPI
from juliao_api.app.api.v1.endpoints import users as users_v1_router
from juliao_api.app.core.config import settings # If settings are needed for app config
# from juliao_api.app.db.session import engine # If you need to connect/disconnect DB on startup/shutdown
# from juliao_api.app.models.base import SQLModel # If using SQLModel base for metadata creation (not with Alembic)

# Potentially add lifespan events for DB connection pool management if not handled by SQLAlchemy engine defaults
# async def lifespan(app: FastAPI):
#     # Connect to DB, etc.
#     yield
#     # Disconnect DB, etc.

app = FastAPI(
    title="Julião API",
    description="Backend API for the Julião personal finance application.",
    version="0.1.0",
    # lifespan=lifespan # Uncomment if lifespan events are defined
)

# Include health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "API is healthy."}

# Include API routers
app.include_router(
    users_v1_router.router,
    prefix="/api/v1/users",
    tags=["Users - v1"]
)

# Further routers can be added here, e.g., for transactions, budgets, etc.

# Example of how settings might be used if needed at app level
# @app.on_event("startup")
# async def startup_event():
#     print(f"Application startup with Supabase URL: {settings.SUPABASE_URL}")

# Note: If using Alembic for migrations, SQLModel.metadata.create_all(engine)
# should NOT be called here as Alembic handles schema creation.
