#! /bin/python
from sympy import exp, ln, sin, cos
from sympy.abc import x
from chebyshev.approximation import Approximation, get_best_approximation
import numpy

approx1 = get_best_approximation(exp(x), (0, 1), 6, 21)
print("Coefficients for exp(x) on the [0, 1] interval")
print(approx1.get_coeffs())
approx1.print_coeffs_as_table()
print("Maximum error on that interval")
print(approx1.get_error())
print(approx1.get_numpy_error(numpy.exp))
# approx1.plot_absolute_error('|f1-g1|')

approx2 = get_best_approximation(ln(1 + x), (0, 1), 6, 20)
print("Coefficients for ln(1 + x) on the [0, 1] interval")
print(approx2.get_coeffs())
approx2.print_coeffs_as_table()
print("Maximum error on that interval")
print(approx2.get_error())
print(approx2.get_numpy_error(lambda x: numpy.log(1 + x)))
# approx2.plot_absolute_error('|f2-g2|')

approx3 = get_best_approximation(sin(x) / x, (-1, 1), 8, 18)
print("Coefficients for sin(x) / x on the [-1, 1] interval")
print(approx3.get_coeffs())
approx3.print_coeffs_as_table()
print("Maximum error on that interval")
print(approx3.get_error())
print(approx3.get_numpy_error(lambda x: numpy.sin(x) / x))
# approx3.plot_absolute_error('|f3-g3|')

approx4 = get_best_approximation(cos(x), (-1, 1), 8, 18)
print("Coefficients for cos(x) on the [-1, 1] interval")
print(approx4.get_coeffs())
approx4.print_coeffs_as_table()
print("Maximum error on that interval")
print(approx4.get_error())
print(approx4.get_numpy_error(numpy.cos))
# approx4.plot_absolute_error('|f4-g4|')
