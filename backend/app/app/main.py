import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import api_router

app = FastAPI()

origins = ["http://localhost:3000", "http://localhost", "http://192.168.0.9:3000"]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")
