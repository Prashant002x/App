from pywebio.input import *
from pywebio.output import *
import numpy as np
from tensorflow import keras

# Load the saved TensorFlow/Keras model
loaded_model = keras.models.load_model('model.h5')

def predict():
    a = input("Age of Delivery Partner:", type=FLOAT)
    b = input("Ratings of Previous Deliveries:", type=FLOAT)
    c = input("Total Distance:", type=FLOAT)

    features = np.array([[a, b, c]])
    ans = loaded_model.predict(features)
    put_text("Predicted Delivery Time in Minutes =", ans[0][0])

if __name__ == '__main__':
    predict()
