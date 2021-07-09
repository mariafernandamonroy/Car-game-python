from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb+srv://mafemonroy:mafe2218@cluster0.0wqby.mongodb.net/test?authSource=admin&replicaSet=atlas-10uxrm-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
    client = MongoClient(CONNECTION_STRING)
    db = client['Car_Game_Players']
    return db
