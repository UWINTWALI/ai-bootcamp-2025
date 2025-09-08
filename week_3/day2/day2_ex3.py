"""
Singular Value Decomposition (SVD) Example Script

Purpose:
    Demonstrates how to perform Singular Value Decomposition (SVD) on a square matrix using the NumPy library in Python, and how to reconstruct the original matrix from its SVD components.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, especially with arrays and matrices.
      - np.linalg: NumPy's linear algebra module, which provides advanced matrix operations such as SVD.

Variables:
    - A: A 3x3 NumPy array (matrix) with elements [[3, 1, 1], [-1, 3, 1], [1, 1, 3]].
    - U: The left singular vectors of matrix A, computed using np.linalg.svd(A).
    - S: The singular values of matrix A, computed using np.linalg.svd(A).
    - Vt: The transpose of the right singular vectors of matrix A, computed using np.linalg.svd(A).
    - Sigma: A 3x3 diagonal matrix with the singular values S on its diagonal, used for reconstruction.
    - reconstructed: The matrix reconstructed from U, Sigma, and Vt using matrix multiplication.

Operations Demonstrated:
    - Performing SVD using np.linalg.svd().
    - Constructing the diagonal Sigma matrix from the singular values.
    - Reconstructing the original matrix using matrix multiplication (the @ operator).
    - Printing the SVD components and the reconstructed matrix.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like numpy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - @: The matrix multiplication operator in Python (introduced in Python 3.5+).
    - print(): A built-in function to display output to the console.

Note:
    - 'linalg' stands for "linear algebra" and is a submodule of numpy that provides functions for advanced matrix operations, including SVD.

Intended Audience:
    Learners new to NumPy, SVD, and matrix operations in Python.
"""
import numpy as np

A = np.array([[3, 1, 1], [-1, 3, 1], [1, 1, 3]])
U, S, Vt = np.linalg.svd(A)

print("U:\n", U)
print("Singular Values:\n", S)
print("V Transpose:\n", Vt)

# Reconstruct
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed Matrix \n", reconstructed)