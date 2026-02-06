from fastapi import APIRouter

health_router = APIRouter(prefix="/v1/health")



@health_router.get('/')
def health_check():
    return {"status": "ok"}
