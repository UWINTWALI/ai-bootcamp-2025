"""
Matrix-Vector Multiplication Example Script

Purpose:
    Demonstrates how to perform matrix-vector multiplication using the NumPy library in Python.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, especially with arrays and matrices.

Variables:
    - M: A 3x3 NumPy array (matrix) with elements [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
    - v: A 1D NumPy array (vector) with elements [1, 0, -1].
    - result: The resulting vector from multiplying matrix M by vector v using np.dot().

Operations Demonstrated:
    - Matrix-vector multiplication using np.dot(M, v), which computes the dot product of M and v.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like numpy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to NumPy and matrix operations in Python.
"""
import numpy as np

# Create matrix and vector
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, -1])

# Matrix-vector multiplication 
result = np.dot(M, v)
print("Matrix-Vector Multiplication: \n", result)