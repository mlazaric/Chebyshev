#! /bin/python
from sympy import exp, ln, sin, cos
from sympy.abc import x
from chebyshev_approximation import Approximation

approx1 = Approximation(exp(x), (0, 1), 6)
print(approx1.get_coeffs())
print(approx1.get_error())
#approx1.plot_absolute_error()

approx2 = Approximation(ln(1 + x), (0, 1), 6)
print(approx2.get_coeffs())
print(approx2.get_error())

approx3 = Approximation(sin(x) / x, (-1, 1), 8)
print(approx3.get_coeffs())
print(approx3.get_error())

approx4 = Approximation(cos(x), (-1, 1), 8)
print(approx4.get_coeffs())
print(approx4.get_error())
