import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.urls

url_collection = database.get_collection("students_collection")


# helpers

def url_helper(url) -> dict:
    return {
        "long_url": str(url["long_url"]),
        "id": str(url["_id"]),
        "short_url": str(url["short_url"])

    }


async def add_url(long_url: str):
    url = await url_collection.insert_one(long_url)
    new_url = await url_collection.find_one({"_id" : ObjectId(id)})
    return url_helper(url)


async def retrive(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)
