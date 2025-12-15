from pymongo import MongoClient
from ..core.settings import settings

"""
Get the async db connection
"""
def get_db():
    uri = settings.mongo_url
    client = MongoClient(uri)
    db = client[settings.mongo_db]
    return db

db = get_db()