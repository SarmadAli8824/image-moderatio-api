import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["moderation_db"]
tokens_collection = db["tokens"]
usages_collection = db["usages"]