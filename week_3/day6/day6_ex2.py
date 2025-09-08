"""
Independent Two-Sample t-Test Example Script

Purpose:
    Demonstrates how to perform an independent two-sample t-test to compare the means of two groups and interpret the statistical significance of the result.

Description:
    The script defines two sample datasets (group1 and group2) and uses the ttest_ind function to test whether their means are significantly different. It prints the t-statistic and p-value, then interprets the result based on a significance level (alpha).

Variables:
    - group1, group2: Lists of numerical values representing two independent samples.
    - t_stat: The calculated t-statistic from the t-test.
    - p_value: The probability of observing the data if the null hypothesis is true.
    - alpha: The significance level threshold (commonly set at 0.05).

Python Keywords/Concepts Introduced:
    - from ... import ...: Imports a specific function (ttest_ind) from a module.
    - if ... else: Conditional statement for interpreting the test result.
    - print(): A built-in function to display output to the console.

Note:
    - The t-test is a fundamental statistical test for comparing the means of two groups.
    - A p-value less than alpha indicates a statistically significant difference between the groups.

Intended Audience:
    Learners new to hypothesis testing, statistical inference, and the use of t-tests in Python.
"""
from scipy.stats import ttest_ind

# Sample Datasets
group1 = [2.1, 2.5, 2.8, 3.0, 3.2]
group2 = [1.8, 2.0, 2.4, 2.7, 2.9]

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Failed to reject the null hypothesis: no significant difference")