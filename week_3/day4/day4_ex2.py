"""
Stochastic Gradient Descent (SGD) for Linear Regression Example Script

Purpose:
    Demonstrates how to implement and use stochastic gradient descent (SGD) to fit a linear regression model on synthetic data using NumPy in Python.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, especially with arrays and matrices.

Variables:
    - X: A (100, 1) NumPy array of randomly generated feature values.
    - y: A (100, 1) NumPy array of target values generated from a linear relationship with noise.
    - X_b: A (100, 2) NumPy array, X with a bias (intercept) column of ones added.
    - theta: A (2, 1) NumPy array of initial model parameters (weights), randomly initialized.
    - learning_rate: A float specifying the step size for each SGD update.
    - n_epochs: An integer specifying the number of passes over the entire dataset.
    - theta_opt: The optimized model parameters after running SGD.

Functions:
    - stochastic_gradient_descent(X, y, theta, learning_rate, n_epocs): Performs SGD to minimize the mean squared error between predictions and targets.

Operations Demonstrated:
    - Generation of synthetic linear data with noise.
    - Addition of a bias term to the feature matrix.
    - Iterative parameter updates using SGD.
    - Printing the optimized parameters.

Python Keywords/Concepts Introduced:
    - def: Used to define a function.
    - for: Used to create loops for epochs and samples.
    - import: Used to bring external libraries (like numpy) into your script.
    - return: Used to return a value from a function.
    - -=: In-place subtraction assignment operator.
    - np.random.seed(): Sets the random seed for reproducibility.
    - np.random.randint(): Generates a random integer for sampling.
    - np.c_: Concatenates arrays along the second axis (used to add bias).
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to machine learning, stochastic gradient descent, and linear regression in Python.
"""
import numpy as np

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term to X
X_b = np.c_[np.ones((100, 1)), X]

# SGD Implementaion
def stochastic_gradient_descent(X, y, theta, learning_rate, n_epocs):
    m = len(y)
    for epoch in range(n_epocs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X[random_index:random_index+1]
            yi = y[random_index:random_index+1]
            gradients = 2 * xi.T @ (xi @ theta - yi)
            theta -= learning_rate * gradients
    return theta

# initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.01
n_epochs = 50

# Perform SGD
theta_opt = stochastic_gradient_descent(X_b, y, theta, learning_rate, n_epochs)
print("Optimized Parameters:", theta_opt)