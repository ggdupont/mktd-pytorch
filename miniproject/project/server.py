import os

from flask import Flask, request
from werkzeug.utils import secure_filename

import cv2

app = Flask(__name__)


@app.route("/process", methods=['POST'])
def serve_prediction():
    print("processing !")
    file = request.files['input']

    filename = '/tmp/uploads/' + secure_filename(file.filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    print('save file at : {}'.format(filename))
    file.save(filename)
    im = cv2.imread(filename)
    print(type(im))

    return str(im.shape)


app.run()
