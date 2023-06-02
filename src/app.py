#!/usr/bin/env python3
import os

from flask import Flask, request
from routes.analysis_routes import register_analysis_routes
from routes.data_routes import register_data_routes

app = Flask(__name__)

register_data_routes(app)
register_analysis_routes(app)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


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


if __name__ == "__main__":
    app.run()
