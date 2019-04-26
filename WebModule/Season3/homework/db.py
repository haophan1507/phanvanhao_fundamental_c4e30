from pymongo import MongoClient

uri = "mongodb+srv://HaoPhan:JcVCpy9IoEWHZ6K9@cluster0-pgtzl.mongodb.net/test?retryWrites=true"
client = MongoClient(uri)
db = client.db_service
bikes_collection = db["bike"]