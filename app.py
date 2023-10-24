from flask import Flask, jsonify, request, redirect, render_template


app = Flask(__name__)

@app.route("/")
def index():
    # return "Flask is running!"
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("hello.html")

    # For post method
    message = request.get_json(force=True)
    name = message["name"]
    response = {
        "greeting": f"Hello, {name}!"
    }
    return jsonify(response)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    ...
    if request.method == "GET":
        return render_template("predict.html")
    
    # For post method