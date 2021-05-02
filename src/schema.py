from mongoengine import Document, StringField
from bson import ObjectId
from datetime import datetime


class UrlSchema(Document):
    id = ObjectId()
    long_Url = StringField(required=True)
    short_Url = StringField(required=True)
    nano_COde = StringField(required=True, unique=True)
