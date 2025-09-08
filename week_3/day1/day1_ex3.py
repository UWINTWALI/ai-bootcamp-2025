"""
Matrix Types Example Script

Purpose:
    Demonstrates how to create and use special types of matrices—identity, diagonal, and zero matrices—using the NumPy library in Python.

Libraries Used:
    - numpy (imported as np): A fundamental library for numerical computations, especially for working with arrays and matrices.

Variables:
    - I: A 3x3 identity matrix created with np.eye(3). The identity matrix has 1s on the diagonal and 0s elsewhere.
    - A: A 3x3 NumPy array (matrix) with elements [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
    - D: A 3x3 diagonal matrix created with np.diag([1, 7, 9]). Only the diagonal elements are nonzero.
    - Z: A 3x3 zero matrix created with np.zeros((3, 3)). All elements are zero.

Operations Demonstrated:
    - Creation of identity, diagonal, and zero matrices.
    - (Commented out) Multiplication of a matrix by the identity matrix using np.dot().
    - Printing the diagonal and zero matrices.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like numpy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to NumPy and special matrix types in Python.
"""

import numpy as np

# Identity Matrix
I = np.eye(3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("A X I:\n", np.dot(A, I))

# Diagonal and Zero Matrix
D = np.diag([1, 7, 9])
Z = np.zeros((3, 3))
print("Diagonal Matrix\n", D)
print("Zero Matrix\n", Z)