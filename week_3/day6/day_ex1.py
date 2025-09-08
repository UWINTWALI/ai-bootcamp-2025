"""
Basic Statistics Calculation Example Script

Purpose:
    Demonstrates how to compute basic statistical measures—mean, variance, and standard deviation—for a dataset using Python.

Description:
    The script defines a simple dataset and calculates its mean, variance, and standard deviation using NumPy functions. These statistics are commonly used to summarize and understand the distribution of numerical data.

Variables:
    - data: A list of numerical values representing the dataset.
    - mean: The average value of the dataset, computed with np.mean().
    - variance: The measure of how much the data varies, computed with np.var().
    - std_dev: The standard deviation, representing the spread of the data, computed with np.std().

Python Keywords/Concepts Introduced:
    - import: Brings external modules (like numpy) into the script.
    - print(): A built-in function to display output to the console.
    - np.mean(), np.var(), np.std(): NumPy functions for calculating mean, variance, and standard deviation.

Note:
    - These statistical functions are essential for data analysis and are widely used in data science and statistics.

Intended Audience:
    Learners new to statistics, data analysis, and NumPy in Python.
"""
import numpy as np

# Dataset
data = [10, 20, 30, 40, 50]

# Calculate Stats
mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

print("Mean: ", mean)
print("Variance: ", variance)
print("Standard Deviation: ", std_dev)