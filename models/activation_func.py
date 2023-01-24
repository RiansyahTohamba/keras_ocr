# activation function
from keras.layers import Dense
from keras.models import Sequential

# output dari sigmoid [0,1]
def sigmoid():
    model = Sequential()
    # Add a dense layer with sigmoid activation
    model.add(Dense(units=64, activation='sigmoid', input_shape=(784,)))

# Here, we are creating a sequential model, and adding a dense layer (also known as a fully connected layer) with 
# '64' units, 
# a sigmoid activation function, and 
# an input shape of 784 (this corresponds to the number of 'features' in the input data).


# output nya adalah multiclass
def relu():
    # Create a sequential model
    model = Sequential()

    # Add a dense layer with softmax activation
    model.add(Dense(units=10, activation='softmax', input_shape=(784,)))

# This example is similar to the previous examples, but in this case, we are using the softmax activation function and the units set to 10, this is because the output classes are 10 .

# Note: the activation functions are set in the Dense layer, which is a fully connected layer in the neural network.

def softmax():
    # Create a sequential model
    model = Sequential()

    # Add a dense layer with relu activation
    model.add(Dense(units=64, activation='relu', input_shape=(784,)))


