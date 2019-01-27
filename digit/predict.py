import numpy as np
import pickle
from PIL import Image
import base64
from io import BytesIO
from digit.twolayernet import TwoLayerNet


def img_prp2(data):
    encoded_image = data.split(",")[1]
    decoded_image = base64.b64decode(encoded_image)
    img = Image.open(BytesIO(decoded_image))
    img_S = img.resize((28, 28))
    im = np.array(img_S)
    im_L = im[:, :, 3]
    if np.sum(im_L) / np.size(im_L) > 100:
        im_LN = 1 - im_L.reshape(1, -1) / 255
    else:
        im_LN = im_L.reshape(1, -1) / 255
    return im_LN


def answer(x):
    with open("digit/0_9642.pkl", 'rb') as f:
        params = pickle.load(f)
    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10, params=params, dropout_ratio=0)

    answer = network.predict(x)
    answer = np.argmax(answer, axis=1)

    return answer
