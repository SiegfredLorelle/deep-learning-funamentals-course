from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def index():
    return "Flask is running!"

@app.route("/hello", methods=["POST"])
def hello():
    message = request.get_json(force=True)
    name = message["name"]
    response = {
        "greeting": f"Hello, {name}!"
    }
    return jsonify(response)