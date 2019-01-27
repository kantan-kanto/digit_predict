import numpy as np
from collections import OrderedDict
from digit.layers import *

class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, params, weight_init_std=0.01, dropout_ratio=0.5):
        self.params = params

        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['BatchNormalization1']=BatchNormalization(self.params['gamma1'], self.params['beta1'])
        self.layers['Relu'] = Relu()
        self.layers['Dropout'] = Dropout(dropout_ratio)
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()


    def predict(self, x, train_flg=False):
        for layer in self.layers.values():
            x = layer.forward(x, train_flg)
        return x
