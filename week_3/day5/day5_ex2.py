"""
Probability Distributions Visualization Example Script

Purpose:
    Demonstrates how to visualize common probability distributions—Gaussian (Normal), Binomial, and Poisson—using NumPy, Matplotlib, and SciPy in Python.

Libraries Used:
    - numpy (imported as np): Used for numerical operations and generating ranges of values.
    - matplotlib.pyplot (imported as plt): Used for plotting and visualizing data.
    - scipy.stats: Provides probability distribution functions for statistical analysis.
        - norm: For Gaussian (Normal) distribution.
        - binom: For Binomial distribution.
        - poisson: For Poisson distribution.

Distributions Demonstrated:
    - Gaussian (Normal) Distribution: Continuous distribution, visualized using norm.pdf().
    - Binomial Distribution: Discrete distribution, visualized using binom.pmf().
    - Poisson Distribution: Discrete distribution, visualized using poisson.pmf().

Variables:
    - x: Array of values over which the probability distribution is evaluated.
    - y: Probability values for each x, computed using the respective distribution's PDF or PMF.
    - n, p: Parameters for the binomial distribution (number of trials and probability of success).
    - lam: Lambda (rate) parameter for the Poisson distribution.

Operations Demonstrated:
    - Generating value ranges for plotting.
    - Computing probability values for each distribution.
    - Plotting distributions using line plots (for Gaussian) and bar plots (for Binomial and Poisson).
    - Setting plot titles and displaying plots.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (numpy, matplotlib, scipy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'numpy as np').
    - from ... import ...: Used to import specific functions or classes from a module.
    - plt.plot(), plt.bar(), plt.title(), plt.show(): Functions from matplotlib for creating and displaying plots.

Note:
    - The script contains commented-out sections for Gaussian and Binomial distributions; uncomment to visualize those as well.
    - The Poisson distribution plot is active by default.

Intended Audience:
    Learners new to probability distributions, statistical visualization, and scientific computing in Python.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson 

# Gausian Distribution
# x = np.linspace(-4, 4, 100)
# y = norm.pdf(x, loc=0, scale=1)
# plt.plot(x, y, label="Gaussian")
# plt.title("Gaussian Distribution")
# plt.show()

# Binomial Distribution
# n, p = 10, 0.5
# x = np.arange(0, n+1)
# y = binom.pmf(x, n, p)
# plt.bar(x, y, label="Binomial")
# plt.title("Binomial Distribution")
# plt.show()

# Poisson Distribution
lam =3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, label="Poisson")
plt.title("Poisson Distribution")
plt.show()