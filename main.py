from fastapi import FastAPI
from src.schema import UrlSchema
from src.models import Url
import os
import nanoid


app = FastAPI()
'''@app.post("/")
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
'''

@app.post("/", response_model= dict)
def shorty(url : UrlSchema):

    url = dict(url)
    nano_Code = nanoid.generate(size=8)
    short_Url = os.path.join("BASE_URL", nano_Code)
    return short_Url

