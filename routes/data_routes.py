from flask import Blueprint, jsonify
from data.collect import collect_data

from utils.database import get_db

data_routes = Blueprint("data_routes", __name__)


@data_routes.route("/api/listing", methods=["GET"])
def get_data():
    db = get_db()["raw_data"]
    data = db.find()
    # convert the Cursor object to a list of dictionaries
    data_list = []
    for doc in data:
        doc["_id"] = str(doc["_id"])
        data_list.append(doc)

    return jsonify(data_list)


@data_routes.route("/api/listing", methods=["POST"])
def create_data():
    try:
        collect_data()

        return jsonify({"message": "Data collection completed."})
    except Exception as e:
        return jsonify({"error": str(e)})


def register_data_routes(app):
    app.register_blueprint(data_routes)
