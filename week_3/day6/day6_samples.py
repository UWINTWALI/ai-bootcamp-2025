"""
Basic Statistics and Confidence Interval Calculation Example Script

Purpose:
    Demonstrates how to manually compute basic statistical measures (mean, variance, standard deviation) and a 95% confidence interval for a dataset. Also includes (commented out) examples for calculating median and mode.

Description:
    The script defines a dataset and calculates its mean, variance, and standard deviation using pure Python (no NumPy). It then computes a 95% confidence interval for the mean using the z-score for a normal distribution. Additional (commented) code shows how to compute median and mode.

Variables:
    - data: List of numerical values representing the dataset.
    - mean: The average value of the dataset.
    - variance: The average of squared differences from the mean.
    - std_dev: The standard deviation, representing the spread of the data.
    - z_score: The z-value for a 95% confidence interval (1.96).
    - ci: Tuple representing the lower and upper bounds of the confidence interval.

Python Keywords/Concepts Introduced:
    - import ... as ...: Imports a module and assigns it an alias for easier reference.
    - sum(), len(): Built-in functions to sum elements and get the length of a list.
    - for ... in ...: Looping construct used in list comprehensions.
    - **: Exponentiation operator (e.g., x ** 2 for squaring).
    - if ... else: Conditional expression for calculating the median.
    - print(): A built-in function to display output to the console.
    - (commented) from ... import ...: Imports a specific function (mode) from a module.

Note:
    - The confidence interval calculation assumes a normal distribution and uses the z-score for 95% confidence.
    - The script demonstrates both manual and library-based approaches (see commented code) for basic statistics.

Intended Audience:
    Learners new to statistics, confidence intervals, and basic Python data analysis.
"""
import scipy.stats as stats


data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5

sample_mean = mean
z_score = 1.96

ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5),
      sample_mean + z_score * (std_dev / len(data) ** 0.5))
print("95% Confidence Interval:", ci) 



# from statistics import mode

# data = [10, 20, 30, 40, 50]
# mean = sum(data) / len(data)
# print("Mean: ", mean)

# sorted_data = sorted(data)
# median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else \
#     (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
# print("Median: ", median)

# print("Mode: ", mode(data))

# variance = sum((x - mean) ** 2 for x in data) / len(data)
# print("Variance: ", variance)
# std_dev = variance ** 0.5
# print("Standard Deviation:", std_dev)