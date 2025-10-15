from pymongo import MongoClient

MONGO_URI = "mongodb://user:password@localhost:27017/admin"

def connect2DB():
    client = MongoClient(MONGO_URI,serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
    return client


if __name__ == '__main__':
    client = connect2DB()

    # Exercice 2
    # 1. Créez une nouvelle base de données appelée CinemaDB
    db = client['CinemaDB']
    collection = db['Films']
    git





