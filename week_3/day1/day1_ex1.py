"""
Matrix Operations Example Script

This script demonstrates basic matrix operations using the NumPy library in Python.
It covers matrix creation, addition, subtraction, and scalar multiplication.

Libraries Used:
- numpy (imported as np): A powerful library for numerical computations, especially with arrays and matrices.

Variables:
- A: A 2x2 NumPy array (matrix) with elements [[1, 2], [3, 4]].
- B: A 2x2 NumPy array (matrix) with elements [[9, 8], [7, 6]].

Operations Demonstrated:
- Addition (A + B): Element-wise addition of matrices A and B.
- Subtraction (A - B): Element-wise subtraction of matrix B from A.
- Scalar Multiplication (3 * A): Multiplies every element of matrix A by 3.

Python Keywords/Concepts Introduced:
- import: Used to bring external libraries (like numpy) into your script.
- as: Used to give an imported module a shorter alias (e.g., 'numpy as np').
- print(): A built-in function to display output to the console.

This script is intended for learners new to NumPy and matrix operations in Python.
"""

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[9, 8], [7, 6]])

# Addition
print("Addition\n", A + B)

# Subtraction
print("Subtraction\n", A - B)

# Scalar Multiplication
print("Scalar Mult: \n", 3 * A)