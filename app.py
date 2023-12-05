from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the pre-trained model
model = load_model(os.path.join("artifacts", "trained_model", "model.h5"))


def predict_malaria(image_path):
    test_image = image.load_img(image_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    preds = model.predict(test_image).tolist()[0]
    pred_label = np.argmax(preds)
    pred_prob = np.round(preds[pred_label], 4)

    if pred_label == 0:
        prediction = 'Parasitized'
    else:
        prediction = 'Uninfected'

    return {
        "image": prediction,
        "prediction_label": pred_label,
        "prediction_probability": pred_prob
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['image']

        # Save the uploaded file to a temporary location
        temp_image_path = 'temp_image.jpg'
        uploaded_file.save(temp_image_path)

        # Perform prediction
        prediction_result = predict_malaria(temp_image_path)

        # Display the results on the same page
        return render_template('index.html', prediction_result=prediction_result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
