import logging
from fastapi import FastAPI
from app.routers import router

app = FastAPI()

app.include_router(router)
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"Hello": "World"}