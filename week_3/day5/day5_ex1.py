"""
Bayes' Theorem for Medical Test Probability Example Script

Purpose:
    Demonstrates how to use Bayes' Theorem to calculate the probability of having a disease given a positive test result, based on disease prevalence, test sensitivity, and test specificity.

Problem Context:
    - A disease affects 1% of a population.
    - The test correctly identifies diseased individuals 95% of the time (sensitivity).
    - The test correctly identifies non-diseased individuals 90% of the time (specificity).
    - The goal is to find the probability that a person actually has the disease given a positive test result.

Variables:
    - prior: The prior probability (prevalence) of the disease in the population (float).
    - sensitivity: The probability that the test is positive given the person has the disease (true positive rate, float).
    - specificity: The probability that the test is negative given the person does not have the disease (true negative rate, float).
    - posterior: The probability of having the disease given a positive test result (float), computed using Bayes' Theorem.

Functions:
    - bayes_theorem(prior, sensitivity, specificity): Calculates the posterior probability using Bayes' Theorem.

Python Keywords/Concepts Introduced:
    - def: Used to define a function.
    - return: Used to return a value from a function.
    - print(): A built-in function to display output to the console.

Note:
    - This script provides a practical example of conditional probability and Bayesian reasoning in medical testing.

Intended Audience:
    Learners new to probability, Bayes' Theorem, and its application in real-world scenarios using Python.
"""
# Problem
# - A disease affects 1% of a population
# - A test is 95% accurate for diseased individuals and 90% accurate for non-diseased individuals
# - Find the probability of having the disease given a positive test result

def bayes_theorem(prior, sensitivity, specificity):
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    posterior = (sensitivity * prior) / evidence
    return posterior

prior = 0.01 # 1% prevalence
sensitivity = 0.95 # True positive rate
specificity = 0.90 # True negative rate

posterior = bayes_theorem(prior, sensitivity, specificity)
print("Probability of Disease Given Positive Test: ", posterior)