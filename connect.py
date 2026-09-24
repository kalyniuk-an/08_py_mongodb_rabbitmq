import os

from dotenv import load_dotenv
from mongoengine import connect


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
connect(host=MONGO_URI)
# url = "mongodb+srv://kalyniukan_db_user:AmatMartin84@cluster0.46ggakh.mongodb.net/?appName=Cluster0"
# connect(host=url)

print("MongoDB connected!")
