#! /bin/python
from chebyshev_approximation import approximate_function
from sympy import plot, exp, Poly, lambdify
from sympy.abc import x
from numpy import linspace

function1 = exp(x)
interval1 = (x, 0, 1)
degree1 = 6
approximation1 = approximate_function(function1, degree1)

for coeff in reversed(Poly(approximation1).all_coeffs()):
    print(float(coeff), end=' ')

curr_x = interval1[1]
err = 0

while curr_x < interval1[2]:
    err = max(abs((function1 - approximation1).subs({x: curr_x})), err)
    curr_x += 0.01
print(err)
plot(abs(function1 - approximation1), interval1)