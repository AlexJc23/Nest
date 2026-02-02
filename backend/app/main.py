from fastapi import FastAPI
from app.core.config import get_settings
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth

settings = get_settings()

app = FastAPI()
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE" ],
    allow_headers=["Authorization", "Content-Type"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
