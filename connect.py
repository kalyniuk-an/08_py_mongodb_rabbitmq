import os

from dotenv import load_dotenv
from mongoengine import connect


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
connect(host=MONGO_URI)

print("MongoDB connected!")
