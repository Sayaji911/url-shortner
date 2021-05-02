from mongoengine import Document, StringField, ObjectIdField
from bson import ObjectId


class Url(Document):
    long_Url = StringField(required=True)
    short_Url = StringField(unique=True)
    nano_Code = StringField(required=True, unique=True)
    id = ObjectId()
