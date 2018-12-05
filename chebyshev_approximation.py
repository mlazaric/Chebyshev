from sympy import Poly, plot, series, degree
from sympy.abc import x
from chebyshev_polynomial import lower_degree_to

class Approximation:
    def __init__(self, function, interval, polynomial_degree):
        self.function = function
        self.interval = interval
        self.polynomial_degree = polynomial_degree

        self.__approximate_function()

    def __approximate_function(self):
        taylor_approximation = series(self.function, x, n=self.polynomial_degree + 5).removeO()

        self.approximation = lower_degree_to(taylor_approximation, self.polynomial_degree)

    def get_coeffs(self):
        coeffs = []

        for coeff in reversed(Poly(self.approximation).all_coeffs()):
            coeffs.append(float(coeff))

        return coeffs

    def get_error(self):
        error = 0
        curr_x = self.interval[0]

        while curr_x < self.interval[1]:
            error = max(abs(float((self.function - self.approximation).subs({x: curr_x}))), error)
            curr_x += 0.01

        return error

    def plot_approximation(self):
        plot(self.approximation, (x, self.interval[0], self.interval[1]))

    def plot_absolute_error(self):
        plot(abs(self.function - self.approximation), (x, self.interval[0], self.interval[1]))