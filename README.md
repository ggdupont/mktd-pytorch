

# Installation

1- Install Anaconda from: https://www.anaconda.com/download
2- Create virtual environment "mktd-pytorch" on python 3.6
```shell
$ conda create -n mktd-pytorch python=3.6
$ conda activate mktd-pytorch
```
3- Install pytorch: `conda install pytorch torchvision -c pytorch`
4- Run the check script:
```shell
$ python checkInstallation.py
```
It should print something like:
```
tensor([[0.1347, 0.7890, 0.1875],
        [0.2210, 0.0476, 0.3556],
        [0.1448, 0.9889, 0.2203],
        [0.1188, 0.8437, 0.1760],
        [0.9675, 0.3313, 0.9360]])
```
The numbers are actually random, so they will differ. But pytorch is correctly installed.

# Exercices

With each exercice will teach you one aspect of deep learning.
The process of machine learning can be decompose in 7 steps :

0. Data acquisition
1. Data preparation
2. Model definition
3. Model training
4. Model evaluation
5. Hyperparameter tuning
6. Prediction

## 1 - Data Preparation

- 1.1 pandas : Load a dataset from CSV file using pandas library
- 1.2 numpy : Use numpy to reshape some arrays
- 1.3 sklearn? : Data normalization (mean and standard deviation)
- 1.4 Training and validation data separation
- 1.5 matplot : visualize images / matrix
- 1.6 matplot : visualize distribution of data by categories 

## 2 - Model definition

- 2.1 Load existing model using h5 files
- 2.2 Print summary (layers) of a model
- 2.3 Create sequential model, add some layers
- 2.4 Save model as h5 file

## 3 - Model training

- 3.1 Metrics : evaluate model
- 3.2 Loss function (mean square error, cross entropy)
- 3.3 Optimizer function (stochastic gradient descent)
- 3.4 Batch size, epoch number
- 3.5 model.compile(training_parameters)
- 3.6 model.fit()
- 3.7 ImageDataGenerator : data
- 3.8 model.fit_generator()

## 4 - Model evaluation

- 4.1 Visualize metrics during training (matplot)
- 4.2 Detect overfitting / underfitting
- 4.2 Validate model with unseen dataset
- 4.3 Visualize confusion matrix

## 6 - Prediction

- 6.1 Create a command line interface to make predictions
- 6.2 Create a web service (REST API) to make predictions

## 5 - Hyperparameter tunning

- 5.1 Use different layers (Dense, Conv2D)
- 5.2 Pooling layer
- 5.3 BatchNormalization, Dropout
- 5.4 Play with training parameters

