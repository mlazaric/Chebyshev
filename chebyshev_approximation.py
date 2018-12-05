from sympy import degree, LC, series
from sympy.abc import x
from chebyshev_polynomial import get_normalised_nth_chebyshev_polynomial

def lower_degree_to(polynomial, n):
    while degree(polynomial) > n:
        normalised_chebyshev_polynomial = get_normalised_nth_chebyshev_polynomial(degree(polynomial))

        polynomial -= normalised_chebyshev_polynomial * LC(polynomial)

    return polynomial

def approximate_function(function, degree):
	taylor_approximation = series(function, x, n = degree + 5).removeO()

	return lower_degree_to(taylor_approximation, degree)