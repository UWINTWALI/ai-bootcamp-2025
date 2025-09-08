"""
day2_ex2.py

This script demonstrates how to generate, filter, and summarize data using NumPy arrays.

Libraries Used:
---------------
- numpy (imported as np): Provides tools for creating and manipulating arrays, as well as mathematical operations.

Variables:
----------
- dataset (numpy.ndarray): A 5x5 array of random integers between 1 and 50 (inclusive).
  Values greater than 25 are replaced with 0 to demonstrate conditional filtering.
- np.sum(dataset): Computes the sum of all elements in the modified dataset.
- np.mean(dataset): Computes the mean (average) of the elements in the modified dataset.
- np.std(dataset): Computes the standard deviation of the elements in the modified dataset.

The script prints the original dataset, the modified dataset after filtering, and summary statistics.
"""
import numpy as np

# Generate random dataset
dataset = np.random.randint(1, 51, size=(5,5))
print("Original: \n", dataset)

# Filter values > 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified Dataset: \n", dataset)


# calculate summary stats
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))