import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from flask import Flask, jsonify, request, redirect, render_template

from helpers import get_model

app = Flask(__name__)


model = get_model("local-notebooks/models/medical_trial_model.h5")

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
    if request.method == "GET":
        return render_template("predict.html")
    
    # For post method
