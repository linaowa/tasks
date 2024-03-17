import numpy as np
import os
import tempfile
from tensorflow import keras
from tensorflow.keras import backend as k
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
import tensorflow as tf
#tf.enable_eager_execution()

if k.backend() != 'tensorflow':
    raise RuntimeError('этот пример может работать только с tensorflow окружением!')

epochs = 20
num_classes = 333

batch_size = 128
buffer_size = 10000

# steps per epoch
spe = int(np.ceil(60000 / float(batch_size))) # = 469

# загрузка данных, уже поделенных на учебную и тестовую часть
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# все знач. цвета в пикселях приводим к одному общему типу и шкале в 255 оттенков
x_train = x_train / 255.0
x_test = x_test / 255.0
# изм. формы тренировочных данных для входного слоя
x_train = x_train.reshape(-1, 28, 28, 1)