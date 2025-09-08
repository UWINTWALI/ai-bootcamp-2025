"""
day_samples.py

This script demonstrates basic usage of the NumPy library for generating random numbers in Python.
It showcases how to create arrays of random floating-point numbers and random integers, which are
commonly used in data analysis, simulations, and machine learning tasks.

Libraries Used:
---------------
- numpy (imported as np): A fundamental package for scientific computing in Python, providing
  support for large, multi-dimensional arrays and matrices, along with a collection of mathematical
  functions to operate on these arrays.

Variables:
----------
- random_array (numpy.ndarray): A 3x3 array of random floating-point numbers sampled from a uniform
  distribution over [0, 1). The random seed is set to 42 for reproducibility.
- random_integers (numpy.ndarray): A 2x3 array of random integers between 0 (inclusive) and 10
  (exclusive), generated using NumPy's randint function.

The script prints both arrays to the console for inspection.

Example Output:
---------------
Random Array: 
 [[0.37454012 0.95071431 0.73199394]
  [0.59865848 0.15601864 0.15599452]
  [0.05808361 0.86617615 0.60111501]]
Random Integers: 
 [[8 7 4]
  [6 9 2]]
"""
import numpy as np

np.random.seed(42)

random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array)


random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)