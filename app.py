from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import plotly.graph_objs as go
import json
import plotly
import logging
from keras.models import model_from_json
import numpy as np
import cv2
from werkzeug.utils import secure_filename
from io import BytesIO
from PIL import Image

import numpy as np
q = [4.0, 12.0, 2.0]
filter1 = [[0, 0, 0, 0, 0],
           [0, -1, 2, -1, 0],
           [0, 2, -4, 2, 0],
           [0, -1, 2, -1, 0],
           [0, 0, 0, 0, 0]]
filter2 = [[-1, 2, -2, 2, -1],
           [2, -6, 8, -6, 2],
           [-2, 8, -12, 8, -2],
           [2, -6, 8, -6, 2],
           [-1, 2, -2, 2, -1]]
filter3 = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, -2, 1, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]


filter1 = np.asarray(filter1, dtype=float) / q[0]
filter2 = np.asarray(filter2, dtype=float) / q[1]
filter3 = np.asarray(filter3, dtype=float) / q[2]

filters = filter1+filter2+filter3

app = Flask(__name__, static_url_path='/static')
app.logger.setLevel(logging.DEBUG)
json_file = open('model.json', "r")
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")


json_file1 = open('phase2_move.json', "r")
loaded_model_json1 = json_file1.read()
json_file1.close()
model1 = model_from_json(loaded_model_json1)
model1.load_weights("phase2_move_weights.h5")

json_file2 = open('phase2_splice.json', "r")
loaded_model_json2 = json_file2.read()
json_file2.close()
model2 = model_from_json(loaded_model_json2)
model2.load_weights("phase2_splice_weights.h5")


img = 0
dict = {0: 'real', 1: 'copy-moved', 2:'spliced'}
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img):
    # Resize the image to the required input size of the model
    img = cv2.resize(img, (48, 48))
    # Convert the image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Preprocess further if needed (e.g., normalize pixel values)
    return img

max_index = None
image1 = None
@app.route('/', methods=['GET', 'POST'])
def login():
    txt = None  
    if request.method == 'POST':
        if 'img' not in request.files:
            return render_template('index.html')

        file = request.files['img']
        if file.filename == '':
            return render_template('index.html')

        if file and allowed_file(file.filename):
            # Read the uploaded image as bytes
            img_bytes = file.read()

            # Convert the bytes to a PIL image
            pil_image = Image.open(BytesIO(img_bytes))

            # Convert the PIL image to an OpenCV image
            opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            # Preprocess the image
            processed_img = preprocess_image(opencv_image)

            # Expand dimensions to match model input shape
            cropped_img = np.expand_dims(np.expand_dims(processed_img, -1), 0)

            # Assuming you have a pre-trained model named "model"
            pred = model.predict(cropped_img)
            max_index = int(np.argmax(pred))
            txt = dict[max_index]
    return render_template('index.html', txt = txt)






app.run(debug=True)
