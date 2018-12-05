#! /bin/python
from sympy import exp, ln, sin, cos
from sympy.abc import x
from chebyshev_approximation import Approximation

approx1 = Approximation(exp(x), (0, 1), 6)
print("Coefficients for exp(x) on the [0, 1] interval")
print(approx1.get_coeffs())
print("Maximum error on that interval")
print(approx1.get_error())
#approx1.plot_absolute_error()

approx2 = Approximation(ln(1 + x), (0, 1), 6)
print("Coefficients for ln(1 + x) on the [0, 1] interval")
print(approx2.get_coeffs())
print("Maximum error on that interval")
print(approx2.get_error())

approx3 = Approximation(sin(x) / x, (-1, 1), 8)
print("Coefficients for sin(x) / x on the [-1, 1] interval")
print(approx3.get_coeffs())
print("Maximum error on that interval")
print(approx3.get_error())

approx4 = Approximation(cos(x), (-1, 1), 8)
print("Coefficients for cos(x) on the [-1, 1] interval")
print(approx4.get_coeffs())
print("Maximum error on that interval")
print(approx4.get_error())
