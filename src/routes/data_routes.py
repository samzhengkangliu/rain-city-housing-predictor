from flask import Blueprint, jsonify, request

from src.utils.database import get_db_connection

data_routes = Blueprint("data_routes", __name__)


@data_routes.route("/api/data", methods=["GET"])
def get_data():
    # Retrieve data from the database or any other source
    db = get_db_connection()
    data = db.query("SELECT * FROM data_table").fetchall()
    return jsonify(data)


@data_routes.route("/api/data", methods=["POST"])
def create_data():
    # Process and save the incoming data
    data = request.get_json()
    # ...

    return jsonify({"message": "Data created successfully"}), 201


def register_data_routes(app):
    app.register_blueprint(data_routes)
