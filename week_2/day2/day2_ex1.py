"""
day2_ex1.py

This script demonstrates basic NumPy operations with arrays, including broadcasting and scalar multiplication.

Libraries Used:
---------------
- numpy (imported as np): Provides support for large, multi-dimensional arrays and matrix operations.

Variables:
----------
- matrix (numpy.ndarray): A 3x3 array containing integers from 1 to 9.
- vector (numpy.ndarray): A 1D array with three elements: [1, 0, -1].
- result_add (numpy.ndarray): The result of adding 'vector' to each row of 'matrix' using broadcasting.
- result_mul (numpy.ndarray): The result of multiplying each element of 'matrix' by 2.

The script prints the results of both operations to the console.
"""
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0 , -1])

result_add = matrix + vector
print("Add: \n", result_add)

result_mul = matrix * 2
print("Multiplication: \n", result_mul)
