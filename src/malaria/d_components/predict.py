import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join(
            "artifacts", "trained_model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        preds = model.predict(test_image).tolist()[0]
        pred_label = np.argmax(preds)
        pred_prob = np.round(preds[pred_label], 4)

        if pred_label == 0:
            prediction = 'Parasitized'
            return [{"image": prediction,
                     "prediction_label": pred_label,
                     "prediction_probability": pred_prob}]
        else:
            prediction = 'Uninfected'
            return [{"image": prediction,
                     "prediction_label": pred_label,
                     "prediction_probability": pred_prob}]
