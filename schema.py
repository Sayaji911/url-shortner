from typing import Optional
from pydantic import BaseModel, validator, constr

import validators


class UrlSchema(BaseModel):
    longUrl: str
    customCode: Optional[constr(max_length=8)] = None

    @validator('longUrl')
    def validate_url(cls, v):
        if not validators.url(v):
            raise ValueError("Long URL is invalid.")
        return v
