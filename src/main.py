"main module"
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.routes import upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.upload_route)

@app.get('/')
def hello_world():
    return {"message": "Hello World!!!"}

app.mount("/static", StaticFiles(directory="./img"), name="static")