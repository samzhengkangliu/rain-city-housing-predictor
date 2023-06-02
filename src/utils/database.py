from pymongo import MongoClient


def get_db_connection():
    connection_string = "mongodb+srv://admin:<password>@@rain-city.fyggiu8.mongodb.net?retryWrites=true&w=majority"

    client = MongoClient(connection_string)
    db = client.housing
    return db
