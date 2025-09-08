"""
Gradient Descent for Linear Regression Example Script

Purpose:
    Demonstrates how to implement and use the gradient descent optimization algorithm to fit a linear regression model using NumPy in Python.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, especially with arrays and matrices.

Variables:
    - X: A NumPy array representing the feature matrix (with a bias column), shape (3, 2).
    - y: A NumPy array representing the target values, shape (3,).
    - theta: A NumPy array of initial model parameters (weights), shape (2,).
    - learning_rate: A float specifying the step size for each iteration of gradient descent.
    - iterations: An integer specifying the number of iterations for the optimization loop.
    - optimized_theta: The optimized model parameters after running gradient descent.

Functions:
    - gradient_descent(X, y, theta, learning_rate, iterations): Performs gradient descent to minimize the mean squared error between predictions and targets.

Operations Demonstrated:
    - Calculation of predictions and errors.
    - Computation of gradients and parameter updates.
    - Iterative optimization of model parameters.
    - Printing the optimized parameters.

Python Keywords/Concepts Introduced:
    - def: Used to define a function.
    - for: Used to create a loop for a fixed number of iterations.
    - import: Used to bring external libraries (like numpy) into your script.
    - return: Used to return a value from a function.
    - -=: In-place subtraction assignment operator.
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to machine learning, gradient descent, and linear regression in Python.
"""
import numpy as np

# Define the gradient descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = (1/m) * np.dot(X.T, errors)
        theta -= learning_rate * gradients
    return theta

# Sample Data
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([2, 2.5, 3.5])
theta = np.array([0.1, 0.1])
learning_rate = 0.1
iterations = 1000

# Perform gradinet descent
optimized_theta = gradient_descent(X, y, theta, learning_rate, iterations)

print("Optimized Parameters: ", optimized_theta)