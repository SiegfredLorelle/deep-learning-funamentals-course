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

from helpers import get_model, preprocess_images

app = Flask(__name__)

# Replace this with the path of your saved model
# If you do not have a model, run kaggle-notebooks/convolutional-neural-networks.ipynb to save the model
model = get_model("kaggle-notebooks/models/cats-vs-dogs-(92-test-acc).h5")

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
    message = request.get_json(force=True)
    encoded = message["image"]
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        "prediction": {
            "dog": prediction[0][0],
            "cat": prediction[0][1],
        }
    }

    return jsonify(response)