"""
Symbolic Integration Example Script

Purpose:
    Demonstrates how to perform symbolic integration (both indefinite and definite) of a mathematical function using the SymPy library in Python.

Libraries Used:
    - sympy (imported as sp): A Python library for symbolic mathematics, enabling algebraic manipulation, calculus, and exact integration.

Variables:
    - x: A SymPy symbol representing the variable of integration.
    - f: A symbolic expression representing the function f(x) = exp(-x).
    - indefinite_integral: The indefinite integral (antiderivative) of f with respect to x, computed using sp.integrate(f, x).
    - definite_integral: The definite integral of f from x = 0 to infinity (sp.oo), computed using sp.integrate(f, (x, 0, sp.oo)).

Operations Demonstrated:
    - Defining a symbolic variable and function.
    - Computing the indefinite integral (antiderivative).
    - Computing the definite integral over a specified interval.
    - Printing the results to the console.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like sympy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'sympy as sp').
    - print(): A built-in function to display output to the console.
    - sp.oo: Represents mathematical infinity in SymPy, useful for improper integrals.

Note:
    - SymPy allows for exact symbolic integration, unlike numerical libraries which approximate results.

Intended Audience:
    Learners new to symbolic mathematics and integration in Python.
"""
import sympy as sp

# Define a function
x = sp.Symbol('x')
f = sp.exp(-x)

# Compute indefinite integral
indefinite_integral = sp.integrate(f, x)
print("Indefinite integral: ", indefinite_integral)

# Compute definite integral
definite_integral = sp.integrate(f, (x, 0, sp.oo))
print("Definite Integral: ", definite_integral)