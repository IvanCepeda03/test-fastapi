from fastapi import FastAPI

from app.api.routers import router as v1_router
from app.api.tags import tags_metadata

app = FastAPI(
    title="CODZ Tracker API",
    version="0.0.0",
    contact={
        "name": "Iván Cepeda Álvarez",
        "url": "https://es.linkedin.com/in/ivan-cepeda-alvarez"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=tags_metadata
)

@app.get("/health", tags=["System"])
async def health():
    return {"status": "ok"}  

app.include_router(v1_router)