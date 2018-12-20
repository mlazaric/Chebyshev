from sympy import Poly, plot, series
from sympy.abc import x
from numpy import polyval
from chebyshev.polynomial import lower_degree_to


class Approximation:
    def __init__(self, function, interval, polynomial_degree, taylor_degree=20, point=0):
        self.function = function
        self.interval = interval
        self.polynomial_degree = polynomial_degree

        self.__approximate_function(taylor_degree, point)

    def __approximate_function(self, taylor_degree, point):
        taylor_approximation = series(self.function, x, point, n=taylor_degree).removeO()

        self.approximation = lower_degree_to(taylor_approximation, self.polynomial_degree)

    def get_coeffs(self):
        coeffs = []

        for coeff in reversed(Poly(self.approximation).all_coeffs()):
            coeffs.append(float(coeff))

        return coeffs

    def print_coeffs_as_table(self):
        print('|        Coefficient        |  Term  |')
        print('|---------------------------|--------|')

        for (term, coeff) in Poly(self.approximation).all_terms():
            if coeff == 0:
                continue

            xterm = x ** term[0]
            fcoeff = coeff.evalf(20)

            print(f'| `{fcoeff:+1.20f}` | `{xterm}` |')

    def get_error(self):
        error = 0
        curr_x = self.interval[0]

        while curr_x <= (self.interval[1] + 0.01):
            error = max(abs((self.function - self.approximation).subs({x: curr_x})), error)
            curr_x += 0.01

        return float(error)

    def get_numpy_error(self, function):
        coeffs = self.get_coeffs()
        error = 0
        curr_x = self.interval[0]

        while curr_x <= (self.interval[1] + 0.01):
            error = max(abs(function(curr_x) - polyval(coeffs[::-1], curr_x)), error)
            curr_x += 0.01

        return error

    def plot_approximation(self):
        plot(self.approximation, (x, self.interval[0], self.interval[1]))

    def plot_absolute_error(self, ylabel=''):
        plot(abs(self.function - self.approximation), (x, self.interval[0], self.interval[1]), ylabel=ylabel)


def get_best_approximation(function, interval, polynomial_degree, start_taylor_degree=None, point=0):
    if start_taylor_degree is None:
        start_taylor_degree = polynomial_degree + 1

    prev_approximation = Approximation(function, interval, polynomial_degree, start_taylor_degree, point)
    curr_approximation = Approximation(function, interval, polynomial_degree, start_taylor_degree + 1, point)
    taylor_degree = start_taylor_degree + 2

    while prev_approximation.get_error() > curr_approximation.get_error():
        prev_approximation = curr_approximation
        curr_approximation = Approximation(function, interval, polynomial_degree, taylor_degree, point)
        taylor_degree += 1
        print(taylor_degree)

    return prev_approximation