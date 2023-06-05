from flask import Blueprint, jsonify, request

from data.analysis import (
    build_linear_regression_model,
    generate_data_analysis,
    predict_price,
)

analysis_routes = Blueprint("analysis_routes", __name__)


@analysis_routes.route("/api/model", methods=["GET"])
def build_model():
    try:
        build_linear_regression_model()
        return jsonify("A model has been generated and saved successfully")
    except Exception as e:
        return jsonify({"error": str(e)})


@analysis_routes.route("/api/analysis", methods=["GET"])
def generate_analysis():
    try:
        analysis_result_graphs = generate_data_analysis()

        return jsonify(analysis_result_graphs)
    except Exception as e:
        return jsonify({"error": str(e)})


@analysis_routes.route("/api/predict", methods=["POST"])
def perform_price_prediction():
    try:
        features = request.json
        prediction_result = predict_price(features)

        return jsonify(prediction_result)
    except Exception as e:
        return jsonify({"error": str(e)})


def register_analysis_routes(app):
    app.register_blueprint(analysis_routes)
