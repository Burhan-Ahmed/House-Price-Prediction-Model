# dog-cat-full-dataset
This repository contains 100 images of dogs and cats for training and 25 images of same for testing

I have used this [data](https://www.kaggle.com/c/dogs-vs-cats/data) to prepare this structured data.

20k images is placed in traning and 5k in testing folder.

## Working of Neural Network
Image => Filter => Feature Map => (Max)Pooling => Feature Pool Map => Flatten

# Syntax 
#### Conv2D
`tensorflow.keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid',activation=None, input_shape=None)`
