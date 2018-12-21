from sympy import Poly, plot, series, Expr
from sympy.abc import x
from numpy import polyval
from chebyshev.polynomial import lower_degree_to

from typing import Tuple, Callable, List


class Approximation:
    """
    Class for approximating sympy expressions using the Taylor series and Chebyshev polynomials.
    """

    def __init__(self,
                 function: Expr,
                 interval: Tuple[float, float],
                 polynomial_degree: int,
                 taylor_degree: int = 20,
                 point: float = 0) -> None:
        """
        Creates a new Approximation of the given expression which is approximated with a polynomial of
            degree `polynomial_degree`.

        First it creates a Taylor polynomial of the given `function` with `taylor_degree` degree around
            `point`. Then it lowers the polynomial degree using Chebyshev polynomials until the approximated
            polynomial degree is less than or equal to `polynomial_degree`.

        :param function: sympy expression to approximate
        :param interval: interval on which to approximate (used for calculating error and plotting)
        :param polynomial_degree: maximum degree of the approximation polynomial
        :param taylor_degree: degree of the starting Taylor polynomial
        :param point: point around which to create the Taylor polynomial
        :rtype: None
        """

        self.function = function
        self.interval = interval
        self.polynomial_degree = polynomial_degree

        self.__approximate_function(taylor_degree, point)

    def __approximate_function(self,
                               taylor_degree: int,
                               point: float) -> None:
        """
        Private function for approximating the sympy expression and lowering the Taylor polynomial's degree.

        :param taylor_degree: degree of the starting Taylor polynomial
        :param point: point around which to create the Taylor polynomial
        :rtype: None
        """

        taylor_approximation = Poly(series(self.function, x, point, n=taylor_degree).removeO())

        self.approximation = lower_degree_to(taylor_approximation, self.polynomial_degree)

    @property
    def coeffs(self) -> List[float]:
        """
        Function to get coefficients of the approximation polynomial.

        :return: list of coefficients of the approximation polynomial
        :rtype: List[float]
        """

        return [float(coeff) for coeff in self.approximation.all_coeffs()]

    def print_coeffs_as_table(self) -> None:
        """
        Prints coefficients of the approximation polynomial in a simple markdown table with two columns,
            first column contains the coefficients and the second the terms.

        :rtype: None
        """

        print('|        Coefficient        |  Term  |')
        print('|---------------------------|--------|')

        for (term, coeff) in Poly(self.approximation).all_terms():
            if coeff == 0:
                continue

            xterm = x ** term[0]
            fcoeff = coeff.evalf(20)

            print(f'| `{fcoeff:+1.20f}` | `{xterm}` |')

    def get_error(self,
                  step: float = 0.01) -> float:
        """
        Calculates the maximum absolute error between the given function and the approximation polynomial on the
            interval `interval` with the `step` step.

        :param step: step for calculating error
        :return: maximum error calculated using sympy on the given interval, with the given step
        :rtype: float
        """

        error = 0
        curr_x = self.interval[0]

        while curr_x <= (self.interval[1] + step):
            error = max(abs((self.function - self.approximation).subs({x: curr_x})), error)
            curr_x += step

        return float(error)

    def get_numpy_error(self,
                        function: Callable,
                        step: float = 0.01) -> float:
        """
        Calculates the maximum absolute error between the given function and the approximation polynomial on the
            interval `interval` with the `step` step.

        :param function: a callable function which returns the same result as `function`
        :param step: step for calculating error
        :return: maximum error calculated using numpy on the given interval, with the given step
        :rtype: float
        """
        coeffs = self.coeffs
        error = 0
        curr_x = self.interval[0]

        while curr_x <= (self.interval[1] + step):
            error = max(abs(function(curr_x) - polyval(coeffs, curr_x)), error)
            curr_x += step

        return error

    def plot_approximation(self) -> None:
        """
        Plots the approximation polynomial using sympy's plot function on the given interval.

        :rtype: None
        """

        plot(self.approximation, (x, self.interval[0], self.interval[1]))

    def plot_absolute_error(self,
                            ylabel: str = '') -> None:
        """
        Plots the absolute error between the function and the approximation polynomial using sympy's plot
            on the given interval.

        :param ylabel: label for the y axis
        :rtype: None
        """

        plot(abs(self.function - self.approximation), (x, self.interval[0], self.interval[1]), ylabel=ylabel)


def get_best_approximation(function: Expr,
                           interval: Tuple[float, float],
                           polynomial_degree: int,
                           start_taylor_degree: int = None,
                           point: float = 0) -> Approximation:
    """
    Finds the best approximation by increasing the starting Taylor polynomial degree until the maximum absolute error
        stops decreasing.

    :param function: sympy expression to approximate
    :param interval: interval on which to approximate (used for calculating error and plotting)
    :param polynomial_degree: maximum degree of the approximation polynomial
    :param start_taylor_degree: degree of the starting Taylor polynomial
    :param point: point around which to create the Taylor polynomial
    :return: the approximation with the smallest maximum absolute error
    :rtype: Approximation
    """

    if start_taylor_degree is None:
        start_taylor_degree = polynomial_degree + 1

    prev_approximation = Approximation(function, interval, polynomial_degree, start_taylor_degree, point)
    curr_approximation = Approximation(function, interval, polynomial_degree, start_taylor_degree + 1, point)
    taylor_degree = start_taylor_degree + 2

    while prev_approximation.get_error() > curr_approximation.get_error():
        prev_approximation = curr_approximation
        curr_approximation = Approximation(function, interval, polynomial_degree, taylor_degree, point)
        taylor_degree += 1

    return prev_approximation
