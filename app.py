import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf


class_names = ["Close", "Open", "no_yawn", "yawn"]
app = Flask(__name__)
model = load_model('model.h5', compile=False)

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    if 'imagefile' not in request.files or imagefile.filename == '':
        # No image file was selected
        return render_template('index.html', prediction='No image provided.')
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    # Function to preprocess the image
    def preprocess_image(image_path):
        # Load and resize the image
        img = image.load_img(image_path, target_size=(256, 256))
        # Convert to numpy array
        img_array = image.img_to_array(img)
        img_array_expanded = np.expand_dims(img_array, axis=0)
        return img_array_expanded

    # Function to predict the class of the image
    def predict_image(model, image_path, class_names):
        processed_image = preprocess_image(image_path)
        # Make predictions and find the predicted class
        predictions = model.predict(processed_image)
        predicted_class = class_names[np.argmax(predictions)]
        # Find the predicted probability
        predicted_probability = np.max(predictions)
        return predicted_class, predicted_probability

    # Make the prediction
    predicted_class, predicted_probability = predict_image(model, image_path, class_names)
    classification = f"The image file is: {imagefile.filename}, the predicted class is: {predicted_class}"

    return render_template('index.html', prediction=classification)

if __name__ == '__main__':
    app.run(port=3000, debug=True)