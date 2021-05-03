from pydantic import BaseModel


class UrlSchema(BaseModel):
    long_Url = str
