from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["data_user"]
collection = db["transformed_data"]

documents = collection.find().limit(25)

for doc in documents:
    print(doc)