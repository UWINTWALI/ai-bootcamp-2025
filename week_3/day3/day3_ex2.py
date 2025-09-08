"""
Partial Derivatives (Gradients) Example Script

Purpose:
    Demonstrates how to compute partial derivatives (gradients) of a multivariable function using the SymPy library in Python.

Libraries Used:
    - sympy (imported as sp): A Python library for symbolic mathematics, supporting algebraic manipulation and calculus operations.

Variables:
    - x, y: SymPy symbols representing the variables in the function.
    - f: A symbolic expression representing the function f(x, y) = x**2 + 3*y**2 - 4*x*y.
    - grad_x: The partial derivative of f with respect to x, computed using sp.diff(f, x).
    - grad_y: The partial derivative of f with respect to y, computed using sp.diff(f, y).

Operations Demonstrated:
    - Defining symbolic variables and a multivariable function.
    - Computing partial derivatives with respect to each variable.
    - Printing the computed gradients.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like sympy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'sympy as sp').
    - print(): A built-in function to display output to the console.

Note:
    - SymPy enables exact symbolic computation, making it suitable for calculus and algebraic tasks in Python.

Intended Audience:
    Learners new to symbolic mathematics, partial derivatives, and multivariable calculus in Python.
"""

import sympy as sp


# Define a multivariable function
x, y = sp.symbols('x y')
f = x**2 + 3*y**2 - 4*x*y

# Compute partial derivatives
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Gradients:")
print("Grad X:", grad_x)
print("Grad Y:", grad_y)