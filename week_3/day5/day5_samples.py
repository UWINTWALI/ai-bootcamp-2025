"""
Probability Distributions and Bayes' Theorem Visualization Example Script

Purpose:
    Demonstrates how to visualize several probability distributions (Gaussian, Bernoulli, Binomial, Poisson) and outlines the use of Bayes' Theorem in Python.

Distributions Demonstrated:
    - Gaussian (Normal) Distribution: Continuous distribution, visualized using a probability density function (PDF).
    - Bernoulli Distribution: Discrete distribution for binary outcomes, visualized using a bar plot.
    - Binomial Distribution: Discrete distribution for the number of successes in a fixed number of trials, visualized using binom.pmf().
    - Poisson Distribution: Discrete distribution for the number of events in a fixed interval, visualized using poisson.pmf().

Variables:
    - mu, sigma: Mean and standard deviation for the Gaussian distribution.
    - x: Array of values over which the probability distribution is evaluated.
    - y: Probability values for each x, computed using the respective distribution's PDF or PMF.
    - p: Probability of success for Bernoulli and Binomial distributions.
    - n: Number of trials for the Binomial distribution.
    - lam: Lambda (rate) parameter for the Poisson distribution.

Operations Demonstrated:
    - Generating value ranges for plotting.
    - Computing probability values for each distribution.
    - Plotting distributions using line plots (for Gaussian) and bar plots (for Bernoulli, Binomial, and Poisson).
    - Setting plot titles, axis labels, and displaying plots.

Python Keywords/Concepts Introduced:
    - import: Brings external modules into the script.
    - as: Assigns a short alias to an imported module.
    - from ... import ...: Imports specific functions or classes from a module.
    - plt.plot(), plt.bar(), plt.title(), plt.xticks(), plt.show(): Functions for creating and displaying plots.
    - np.linspace(): Generates evenly spaced numbers over a specified interval.
    - np.arange(): Generates a range of values with a given step size.
    - binom.pmf(), poisson.pmf(): Probability mass functions for Binomial and Poisson distributions.

Note:
    - Several sections are commented out; uncomment them to visualize the corresponding distributions.
    - The script provides a practical introduction to probability distributions and their visualization in Python.

Intended Audience:
    Learners new to probability, probability distributions, and data visualization in Python.
"""
# def bayes_theorem(prior, likelihood, evidence):
#     return (likelihood * prior) / evidence

import numpy as np
import matplotlib.pyplot as plt

# mu, sigma = 0, 1
# x = np.linspace(-4, 4, 100)
# y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# plt.plot(x, y)
# plt.title("Gaussian Distribution")
# plt.show()

# p = 0.6
# plt.bar([0, 1], [1-p, p], color="blue")
# plt.title("Bernoulli Distribution")
# plt.xticks([0, 1], labels=["0 (Failure)", "1 (Success)"])
# plt.show()

from scipy.stats import binom

# n, p = 10, 0.5
# x = np.arange(0, n+1)
# y = binom.pmf(x, n, p)
# plt.bar(x, y, color="green")
# plt.title("Binomial Distribution")
# plt.show()

from scipy.stats import poisson

lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, color="orange")
plt.title("Poisson Distribution")
plt.show()

