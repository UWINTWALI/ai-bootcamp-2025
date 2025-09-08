"""
Symbolic Integration Example Script

Purpose:
    Demonstrates how to perform both definite and indefinite symbolic integration of a mathematical function using the SymPy library in Python.

Libraries Used:
    - sympy (imported as sp): A Python library for symbolic mathematics, enabling algebraic manipulation and exact calculus operations.

Variables:
    - x: A SymPy symbol representing the variable of integration.
    - f: A symbolic expression representing the function f(x) = x**2.
    - definite_integral: The definite integral of f from x = 0 to x = 2, computed using sp.integrate(f, (x, 0, 2)).
    - indefinite_integral: The indefinite integral (antiderivative) of f with respect to x, computed using sp.integrate(f, x).

Operations Demonstrated:
    - Defining a symbolic variable and function.
    - Computing the definite integral over a specified interval.
    - Computing the indefinite integral (antiderivative).
    - Printing the results to the console.

Python Keywords/Concepts Introduced:
    - import: Used to bring external libraries (like sympy) into your script.
    - as: Used to assign a short alias to an imported module (e.g., 'sympy as sp').
    - print(): A built-in function to display output to the console.
    - sp.integrate(): Performs symbolic integration, supporting both definite and indefinite integrals.

Note:
    - SymPy allows for exact symbolic integration, unlike numerical libraries which approximate results.

Intended Audience:
    Learners new to symbolic mathematics and integration in Python.
"""
import sympy as sp

x = sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 2))
indefinite_integral = sp.integrate(f, x)
print("Definite Integral:", definite_integral)
print("Indefinite Integral:", indefinite_integral)