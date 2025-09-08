"""
Matrix Operations and Special Matrices Example Script

Purpose:
    Demonstrates a variety of basic matrix operations and the creation of special matrices using the NumPy library in Python.

Libraries Used:
    - numpy (imported as np): A widely-used library for numerical computations, particularly with arrays and matrices.

Variables:
    - A: A 2x2 NumPy array (matrix) with elements [[1, 2], [3, 4]].
    - B: A 2x2 NumPy array (matrix) with elements [[5, 6], [7, 8]].
    - C: Result of scalar multiplication (2 * A), multiplying every element of A by 2.
    - result: The result of matrix multiplication of A and B using np.dot(A, B).
    - I: A 5x5 identity matrix created with np.eye(5), having 1s on the diagonal and 0s elsewhere.
    - Z: A 2x3 zero matrix created with np.zeros((2, 3)), where all elements are zero.
    - D: A 3x3 diagonal matrix created with np.diag([1, 2, 3]), where only the diagonal elements are nonzero.

Operations Demonstrated:
    - Matrix addition and subtraction (commented out).
    - Scalar multiplication of a matrix.
    - Matrix multiplication using np.dot().
    - Creation of identity, zero, and diagonal matrices.
    - Printing of the diagonal matrix.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like numpy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - print(): A built-in function to display output to the console.

Intended Audience:
    Learners new to NumPy and matrix operations in Python.
"""
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# print("Addition: \n", A + B)
# print("Subtraction: \n", B - A)

C = 2 * A
# print("Scalar Multiplication \n", C)

result = np.dot(A, B)

# print("Matrix Multiplication \n", result)

I = np.eye(5)
# print("Identity Matrix \n", I)

Z = np.zeros((2, 3))
# print("Zero Matrix \n", Z)

D = np.diag([1, 2, 3])
print("Diagonal Matrix\n", D)




