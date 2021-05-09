from fastapi import FastAPI,Request
from router.shortit import router as ShortenRouter
from router.redirect import router as RedirectRouter
from mongoengine import connect
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates
from decouple import config

BASE_URL = "http://localhost:8000"
MODEL_URL = " Yor MongoDB URL"

#MODEL_URL = config('MODEL_URL')

print(MODEL_URL)

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="template")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(ShortenRouter, tags=["Shorten long URL"], prefix="/api/v1/shortit")

app.include_router(RedirectRouter, tags=["Redirect to Short URL"])


@app.on_event("startup")
async def create_db_client():
    try:
        connect(host=MODEL_URL)
        print("Successfully connected to Mongo Atlas database.")
    except Exception as e:
        print(e)
        print("An error occurred while connecting to Mongo Atlas database.")


@app.on_event("shutdown")
async def shutdown_db_client():
    pass
