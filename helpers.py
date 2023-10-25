# import base64
# import numpy as np
# import io
# from PIL import Image
import tensorflow as tf
from tensorflow import keras
# from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, load_model
# from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array

def get_model(h5_file):
    model = load_model(h5_file)
    print("Model successfully loaded!")
    return model

def preprocess_images(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    return image