import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from routes.analysis_routes import register_analysis_routes
from routes.data_routes import register_data_routes
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Seattle House Price Prediction API"}
)

app = Flask(__name__)

# set the environment variable to the directory containing kaggle.json
load_dotenv(os.path.join(app.root_path, ".env"))

app.register_blueprint(swaggerui_blueprint)
register_data_routes(app)
register_analysis_routes(app)


@app.route("/")
def main():
    return """
    <form action="/echo_user_input" method="POST">
        <input name="user_input">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text


@app.route("/swagger.json")
def serve_swagger_spec():
    return jsonify(generate_swagger_spec(app))


def generate_swagger_spec(app):
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "Seattle House Price Predictor API"
    paths = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint.startswith("data_routes.") or rule.endpoint.startswith(
            "analysis_routes."
        ):
            methods = {}
            for method in rule.methods:
                if method != "HEAD":
                    methods[method.lower()] = {}
            paths[str(rule)] = methods

    swag["paths"] = paths
    return swag


if __name__ == "__main__":
    app.run()
