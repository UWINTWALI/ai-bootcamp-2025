"""
Eigenvalues and Eigenvectors Example Script

Purpose:
    Demonstrates how to compute the eigenvalues and eigenvectors of a square matrix using the NumPy library in Python.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, especially with arrays and matrices.
      - np.linalg: NumPy's linear algebra module, providing functions for matrix operations such as eigenvalue and eigenvector computation.

Variables:
    - A: A 2x2 NumPy array (matrix) with elements [[4, -2], [1, 1]].
    - eigvals: The eigenvalues of matrix A, computed using np.linalg.eig(A).
    - eigvec: The eigenvectors of matrix A, computed using np.linalg.eig(A).

Operations Demonstrated:
    - Calculation of the eigenvalues and eigenvectors of a matrix.
    - Printing the results to the console.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like numpy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to NumPy and basic linear algebra operations in Python.
"""
import numpy as np

A = np.array([[4, -2],[1, 1]])

eigvals, eigvec = np.linalg.eig(A)

print("EigenValues: ",eigvals)
print("EigenVectors: \n",eigvec)