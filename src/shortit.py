from fastapi import FastAPI, APIRouter
from .schema import UrlSchema
from .models import Url
import os
import nanoid

src = APIRouter()


@src.post("/")
async def test(url: UrlSchema):
    url = url
    nano_Code = nanoid.generate(size=8)
    short_Url = os.path.join("BASE_URL", nano_Code)

    url = Url(
        long_Url=url["long_Url"],
        nano_Code=nano_Code,
        short_Url=short_Url
    )
    url.save()

    return {
        "message" :"Shortening Successfull",
        "shortUrl" : short_Url,
        "longURl" : url["long_Url"]
    }

