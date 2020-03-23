from fastapi import APIRouter

from app.api.v1.endpoints import papers, login, users, bookmarks

api_router = APIRouter()
api_router.include_router(papers.router, prefix="/papers", tags=["papers"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(bookmarks.router, prefix="/bookmarks", tags=["bookmarks"])
