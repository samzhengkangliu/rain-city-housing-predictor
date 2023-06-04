#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from flask import Flask, request
from routes.analysis_routes import register_analysis_routes
from routes.data_routes import register_data_routes

app = Flask(__name__)

# Set the environment variable to the directory containing kaggle.json
load_dotenv(os.path.join(app.root_path, '.env'))

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


if __name__ == "__main__":
    app.run()
