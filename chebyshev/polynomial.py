"""
Module for calculating and caching Chebyshev polynomials, as well as
  some helper functions regarding polynomial manipulation.
"""

from sympy import Poly
from sympy.abc import x


"""
Caching for the computed Chebyshev polynomials.
"""
computed_polynomials = [Poly(1, x), Poly(x, x)]


def get_nth_chebyshev_polynomial(polynomial_degree: int) -> Poly:
    """
    Calculates the nth Chebyshev polynomial using the recursive relation:

        T_n = 2x * T_{n - 1} - T_{n - 2}

    Caches the result in the computed_polynomials list.

    :param polynomial_degree: degree of the Chebyshev polynomial
    :return: the nth Chebyshev polynomial
    :rtype: Poly
    """
    if (len(computed_polynomials) - 1) >= polynomial_degree:
        return computed_polynomials[polynomial_degree]

    # T_n = 2x * T_{n - 1} - T_{n - 2}
    T_n_1 = get_nth_chebyshev_polynomial(polynomial_degree - 1)
    T_n_2 = get_nth_chebyshev_polynomial(polynomial_degree - 2)

    T_n = 2 * x * T_n_1 - T_n_2

    computed_polynomials.append(T_n)

    return T_n


def normalise_polynomial(polynomial: Poly) -> Poly:
    """
    Normalises polynomial by dividing it by its leading coefficient.

    :param polynomial: polynomial to normalise
    :return: normalised polynomial
    :rtype: Poly
    """

    return polynomial / polynomial.LC()


def get_normalised_nth_chebyshev_polynomial(polynomial_degree: int) -> Poly:
    """
    A helper function to return the normalised nth Chebyshev polynomial.

    :param polynomial_degree: degree of the Chebyshev polynomial
    :return: normalised Chebyshev polynomial
    :rtype: Poly
    """

    return normalise_polynomial(get_nth_chebyshev_polynomial(polynomial_degree))


def lower_degree_to(polynomial: Poly,
                    max_polynomial_degree: int) -> Poly:
    """
    Lowers the degree of the polynomial by using Chebyshev polynomials.

    :param polynomial: polynomial to lower the degree of
    :param max_polynomial_degree: maximum polynomial degree to lower to
    :return: polynomial with the degree less than or equal to `max_polynomial_degree`
    :rtype: Poly
    """

    while polynomial.degree() > max_polynomial_degree:
        normalised_chebyshev_polynomial = get_normalised_nth_chebyshev_polynomial(polynomial.degree())

        polynomial -= normalised_chebyshev_polynomial * polynomial.LC()

    return polynomial
