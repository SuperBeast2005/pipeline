from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["data_user"]
collection = db["transformed_data"]

count = collection.count_documents({})
print("Number of documents in collection:", count)

