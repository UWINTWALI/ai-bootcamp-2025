"""
Symbolic Differentiation Example Script

Purpose:
    Demonstrates how to perform symbolic differentiation of a mathematical function using the SymPy library in Python.

Libraries Used:
    - sympy (imported as sp): A Python library for symbolic mathematics, enabling algebraic manipulation and calculus operations.

Variables:
    - x: A SymPy symbol representing the variable 'x' in the function.
    - f: A symbolic expression representing the function f(x) = x**3 - 5*x + 7.
    - derivative: The symbolic derivative of f with respect to x, computed using sp.diff(f, x).

Operations Demonstrated:
    - Defining a symbolic variable and function.
    - Computing the derivative of the function symbolically.
    - Printing the original function and its derivative.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like sympy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'sympy as sp').
    - print(): A built-in function to display output to the console.

Note:
    - SymPy allows for exact, symbolic computation, unlike libraries such as NumPy which are primarily numerical.

Intended Audience:
    Learners new to symbolic mathematics and differentiation in Python.
"""

import sympy as sp

# Define a function
x = sp.Symbol('x')
f = x**3 - 5*x + 7

# Compute Derivative
derivative = sp.diff(f, x)

print("Function: ", f)
print("Derivative: ", derivative)