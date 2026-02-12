from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.exceptions import AppException
from app.schemas.v1.error import ErrorDetail, ErrorResponse

from app.api.v1 import auth, health, users

# temp
from app.db.base import Base
from app.db.database import engine



def create_app() -> FastAPI:
    settings = get_settings()

    # Create FastAPI application instance
    app = FastAPI()
    Base.metadata.create_all(bind=engine)

    # ------------------------
    # Exception Handlers
    # ------------------------
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

    # ------------------------
    # Routers
    # ------------------------
    app.include_router(auth.router)
    app.include_router(health.health_router)
    app.include_router(users.router, prefix="/api/v1")

    # ------------------------
    # Middleware
    # ------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["Authorization", "Content-Type"],
    )

    return app


# ASGI entrypoint
app = create_app()
