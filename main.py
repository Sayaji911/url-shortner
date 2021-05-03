from fastapi import FastAPI, Request, Depends
from src.shortit import src as shortensrc
from mongoengine import connect, disconnect, errors
from decouple import config


app = FastAPI()

MODEL_URL = config("MODEL_URL")


@app.get("/")
async def index(request: Request):
    app.include_router(shortensrc)


@app.on_event("startup")
async def create_db_client():
    try:
        connect(host = MODEL_URL )
        print("Connected")

    except Exception as e:
        print(e)
        print("An error occured")

@app.on_event("shutdown")
async  def shutdown_db_client():
    pass