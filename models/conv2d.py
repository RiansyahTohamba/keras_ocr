def define_lenet5(self):
    model = models.Sequential()
    # 5 Convolutional Layers
    model.add(layers.Conv2D(32, (3, 3), strides=(1, 1), padding='same',
    input_shape=(self.opt.loadHeight, self.opt.loadWidth, 1)))
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(layers.Dropout(self.keep_prob))

# why always sequential?
# A Sequential model in Keras is a linear stack of layers that is a simple and efficient way to create deep learning models. However, it may not always be the best choice for a particular problem or dataset. For example, if the input data has a complex or non-linear relationship with the output, a more advanced architecture such as a non-sequential model may be more suitable. Additionally, the performance of a Sequential model will depend on the specific layers used, the number of layers, and the number of neurons in each layer, as well as the quality and quantity of data available for training.