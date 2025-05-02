from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["data_user"]
collection = db["transformed_data"]

# Get count of all documents
count = collection.count_documents({})
print("Number of documents in collection:", count)