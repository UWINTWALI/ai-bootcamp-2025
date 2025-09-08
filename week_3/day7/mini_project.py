"""
Linear Regression from Scratch with Gradient Descent Example Script

Purpose:
    Demonstrates how to implement linear regression from scratch using NumPy, including synthetic data generation, parameter optimization with gradient descent, and model evaluation with common metrics.

Description:
    The script generates synthetic linear data, adds a bias term, initializes model parameters, and uses gradient descent to optimize the parameters for linear regression. It defines functions for prediction, mean squared error (MSE), and R-squared (R2) evaluation. The optimized parameters and evaluation metrics are printed at the end.

Variables:
    - X: Feature matrix of shape (100, 1), generated randomly.
    - y: Target values, generated from a linear relationship with noise.
    - X_b: Feature matrix with a bias (intercept) column added.
    - theta: Initial model parameters (weights), randomly initialized.
    - learning_rate: Step size for each gradient descent update.
    - iterations: Number of iterations for gradient descent.
    - theta_optimized: Model parameters after optimization.
    - y_pred: Predicted target values using the optimized model.
    - mse: Mean squared error between actual and predicted values.
    - r2: R-squared score, indicating the proportion of variance explained by the model.

Functions:
    - predict(X, theta): Computes predictions for input features using the model parameters.
    - gradient_descent(X, y, theta, learning_rate, iterations): Optimizes model parameters using gradient descent.
    - mean_squared_error(y_true, y_pred): Calculates the mean squared error between true and predicted values.
    - r_squared(y_true, y_pred): Calculates the R-squared score for model evaluation.

Python Keywords/Concepts Introduced:
    - def: Used to define a function.
    - return: Used to return a value from a function.
    - for: Looping construct for repeated operations (gradient descent iterations).
    - -=: In-place subtraction assignment operator, used for parameter updates.
    - np.dot(): Computes the dot product of two arrays (matrix multiplication).
    - np.mean(), np.sum(): NumPy functions for mean and sum calculations.
    - np.c_: Concatenates arrays along the second axis (used to add a bias column).
    - np.random.seed(): Sets the random seed for reproducibility.
    - np.random.rand(), np.random.randn(): Generate random numbers for data and parameter initialization.

Intended Audience:
    Learners new to machine learning, linear regression, gradient descent, and model evaluation in Python.
"""
import numpy as np

# Generate Synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term to feature matrix
X_b = np.c_[np.ones((100, 1)), X]

# Initialze parameters
theta = np.random.randn(2, 1)
learning_rate = 0.1
iterations = 1000

# Task 1: Implement the Mathematical Formula for Linear Regression

def predict(X, theta):
    return np.dot(X, theta)

# Task 2: Use Gradient Descent to Optimize the Model Parameters

def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        gradients = (1/m) * np.dot(X.T, (np.dot(X, theta)- y))
        theta -= learning_rate * gradients
    return theta

# Task 3: Calculate Evaluation Metrics

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)** 2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - (ss_res / ss_tot)  


# Perform gradient descent
theta_optimized = gradient_descent(X_b, y, theta, learning_rate, iterations)

# Predictions and evaluations
y_pred = predict(X_b, theta_optimized)
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized Parameters (Theta): ", theta_optimized)
print("MSE: ", mse)
print("R2: ", r2)