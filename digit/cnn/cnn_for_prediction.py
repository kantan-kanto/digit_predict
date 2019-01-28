from collections import OrderedDict
from digit.cnn.layers import *


class SimpleCNN:

    def __init__(self, params, input_dim=(1, 28, 28),
                 conv_params={'pad': 0, 'stride': 1}, pool_val=2):

        self.params = params
        filter_pad = conv_params['pad']
        filter_stride = conv_params['stride']

        pool_h = pool_val
        pool_w = pool_val
        pool_stride = pool_val

        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(self.params['W1'], self.params['b1'], filter_stride, filter_pad)
        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=pool_h, pool_w=pool_w, stride=pool_stride, pad=0)
        self.layers['Affine1'] = Affine(self.params['W2'], self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

        self.lastLayer = SoftmaxWithLoss()

    def predict(self, x, train_flg=False):
        for layer in self.layers.values():
            x = layer.forward(x, train_flg)

        return x
