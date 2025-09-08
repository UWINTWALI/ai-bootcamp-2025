"""
Symbolic Differentiation and Partial Derivatives Example Script

Purpose:
    Demonstrates how to perform symbolic differentiation and compute partial derivatives of mathematical functions using the SymPy library in Python.

Libraries Used:
    - sympy (imported as sp): A Python library for symbolic mathematics, enabling algebraic manipulation and calculus operations.

Variables:
    - x, y: SymPy symbols representing the variables in the functions.
    - f: A symbolic expression representing the function f(x, y) = x**2 + y**2.
    - grad_x: The partial derivative of f with respect to x, computed using sp.diff(f, x).
    - grad_y: The partial derivative of f with respect to y, computed using sp.diff(f, y).
    - (commented out) derivative: The derivative of f(x) = x**2 with respect to x.

Operations Demonstrated:
    - Defining symbolic variables and functions.
    - Computing derivatives and partial derivatives symbolically.
    - Printing the computed derivatives.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like sympy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'sympy as sp').
    - print(): A built-in function to display output to the console.
    - (commented out) sp.diff(): Computes symbolic derivatives.

Note:
    - SymPy enables exact symbolic computation, making it suitable for calculus and algebraic tasks in Python.

Intended Audience:
    Learners new to symbolic mathematics, differentiation, and partial derivatives in Python.
"""

import sympy as sp

# x = sp.Symbol('x')
# f = x**2
# derivative = sp.diff(f, x)

# print("Derivative: ", derivative)


x, y = sp.symbols('x y')
f = x**2 + y**2
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Partial Derivatives:", grad_x, grad_y)