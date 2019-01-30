import numpy as np
import pickle
from PIL import Image
import base64
from io import BytesIO
from digit.cnn.cnn_for_prediction import SimpleCNN


def img_prp_cnn(data):
    encoded_image = data.split(",")[1]
    decoded_image = base64.b64decode(encoded_image)
    img = Image.open(BytesIO(decoded_image))
    img_S = img.resize((28, 28))
    im = np.array(img_S)
    im_L = im[:, :, 3]
    if np.sum(im_L) / np.size(im_L) > 100:
        im_LN = 1 - im_L.reshape(1, 1, 28, 28) / 255
    else:
        im_LN = im_L.reshape(1, 1, 28, 28) / 255
    return im_LN


def answer_cnn(x):
    with open("digit/cnn/0_9631.pkl", 'rb') as f:
        params = pickle.load(f)

    network = SimpleCNN(params=params)

    answer = network.predict(x)
    answer = np.argmax(answer, axis=1)

    return answer


def pb_cnn(x):
    with open("digit/cnn/0_9631.pkl", 'rb') as f:
        params = pickle.load(f)

    network = SimpleCNN(params=params)

    answer = network.predict(x)
    # answer = np.argmax(answer, axis=1)

    return answer
