#! /bin/python
from sympy import *
from sympy.abc import x

computed_polynomials = [1, x] 

def get_nth_chebyshev_polynomial(n):
    if (len(computed_polynomials) - 1) >= n:
        return computed_polynomials[n] 

    polynomial = simplify(2 * x * get_nth_chebyshev_polynomial(n - 1) 
                                - get_nth_chebyshev_polynomial(n - 2))

    computed_polynomials.append(polynomial)

    return polynomial

def normalise_polynomial(polynomial):
    return polynomial / LC(polynomial)

def lower_degree_to(polynomial, n):
    while degree(polynomial) > n:
        chebyshev_polynomial = get_nth_chebyshev_polynomial(degree(polynomial))
        normalised_polynomial = normalise_polynomial(chebyshev_polynomial)

        polynomial -= normalised_polynomial * LC(polynomial)

    return polynomial

approx = series(ln(1+x), x, n=8).removeO()
print(approx)
approx = simplify(lower_degree_to(approx, 6))
print(approx)
plot(abs(approx - log(1+x)), (x, 0, 1))
