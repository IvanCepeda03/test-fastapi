from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["System"])
async def root():
    return {
        "message": "Welcome to the CODZ Tracker API",
        "version": "0.0.0",
        "documentation": "/docs"
    }