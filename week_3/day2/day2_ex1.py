"""
Determinant and Inverse of a Matrix Example Script

Purpose:
    Demonstrates how to compute the determinant and inverse of a square matrix using the NumPy library in Python.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, especially with arrays and matrices.
      - np.linalg: NumPy's linear algebra module, providing functions for matrix operations such as determinant and inverse.

Variables:
    - A: A 3x3 NumPy array (matrix) with elements [[2, 3, 4], [4, 5, 6], [7, 8, 9]].
    - determinant: The determinant of matrix A, computed using np.linalg.det(A).
    - inverse: The inverse of matrix A, computed using np.linalg.inv(A).

Operations Demonstrated:
    - Calculation of the determinant of a matrix.
    - Calculation of the inverse of a matrix.
    - Printing the results to the console.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like numpy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to NumPy and basic linear algebra operations in Python.
"""
import numpy as np

A = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]])

determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Determinant: ", determinant)
print("Inverse: ", inverse)