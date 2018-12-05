from sympy.abc import x
from sympy import LC, simplify, degree

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

def get_normalised_nth_chebyshev_polynomial(n):
    return normalise_polynomial(get_nth_chebyshev_polynomial(n))

def lower_degree_to(polynomial, n):
    while degree(polynomial) > n:
        normalised_chebyshev_polynomial = get_normalised_nth_chebyshev_polynomial(degree(polynomial))

        polynomial -= normalised_chebyshev_polynomial * LC(polynomial)

    return polynomial