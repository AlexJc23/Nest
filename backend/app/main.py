from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.config import get_settings
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, health, users
from app.exceptions import AppException
from app.schemas.error import ErrorDetail, ErrorResponse


from app.api.users import user_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user_router)
    return app

settings = get_settings()

app = create_app()

# app = FastAPI()

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=ErrorDetail(
                code=exc.code,
                message=exc.message
            )
        ).model_dump()
    )

app.include_router(auth.router)
app.include_router(health.health_router)
app.include_router(users.user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE" ],
    allow_headers=["Authorization", "Content-Type"],
)
