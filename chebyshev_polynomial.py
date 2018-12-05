from sympy.abc import x
from sympy import LC, simplify, degree

computed_polynomials = [1, x]

def get_nth_chebyshev_polynomial(polynomial_degree):
    if (len(computed_polynomials) - 1) >= polynomial_degree:
        return computed_polynomials[polynomial_degree]

    polynomial = simplify(2 * x * get_nth_chebyshev_polynomial(polynomial_degree - 1)
                                - get_nth_chebyshev_polynomial(polynomial_degree - 2))

    computed_polynomials.append(polynomial)

    return polynomial

def normalise_polynomial(polynomial):
    return polynomial / LC(polynomial)

def get_normalised_nth_chebyshev_polynomial(max_polynomial_degree):
    return normalise_polynomial(get_nth_chebyshev_polynomial(max_polynomial_degree))

def lower_degree_to(polynomial, max_polynomial_degree):
    current_polynomial_degree = degree(polynomial)

    while degree(polynomial) > max_polynomial_degree:
        normalised_chebyshev_polynomial = get_normalised_nth_chebyshev_polynomial(current_polynomial_degree)

        polynomial -= normalised_chebyshev_polynomial * LC(polynomial)
        current_polynomial_degree = degree(polynomial)

    return polynomial
