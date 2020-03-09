from fastapi import APIRouter

from app.api.v1.endpoints import papers, login

api_router = APIRouter()
api_router.include_router(papers.router, prefix="/papers", tags=["papers"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
