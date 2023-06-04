from urllib.parse import quote_plus
from pymongo import MongoClient


def get_db():
    username = quote_plus("admin")
    password = quote_plus("cl9gKwzk133f1ho8")
    cluster_url = "rain-city.fyggiu8.mongodb.net"
    database_name = "house_listing_data"

    connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/{database_name}?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(connection_string)
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client["seattle"]
    except Exception as e:
        print(e)
