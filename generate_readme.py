#! /bin/python
import re
from sympy import exp, ln, sin, cos
from sympy.abc import x

from chebyshev.approximation import get_best_approximation

table_of_contents = []
function_entries = []


def generate_for_readme(approximation):
    function_filename = re.sub(r'( |/)', '_', str(approximation.function))
    approximation_plot_filename = f'images/{function_filename}_approximation.png'
    absolute_error_plot_filename = f'images/{function_filename}_absolute_error.png'

    table_of_contents.append((str(approximation.function),
                              re.sub(r'(\+|/|\(|\))', '', str(approximation.function))
                              .replace(' ', '-')))

    function_entries.append(f"""## `{approximation.function}`

Coefficients for `{approximation.function}` on the `[{approximation.interval[0]}, {approximation.interval[
        1]}]` interval:
     
{approximation.get_coeffs_as_table()}

Maximum error on that interval is `{approximation.get_error()}`

<img src="{approximation_plot_filename}" alt="{approximation_plot_filename}" width="50%"><img src="{absolute_error_plot_filename}" alt="{absolute_error_plot_filename}" width="50%">
""")

    plotted = approximation.plot_approximation(show=False)
    backend = plotted.backend(plotted)
    backend.process_series()
    backend.fig.savefig(approximation_plot_filename, dpi=300)

    plotted = approximation.plot_absolute_error(show=False)
    backend = plotted.backend(plotted)
    backend.process_series()
    backend.fig.savefig(absolute_error_plot_filename, dpi=300)


generate_for_readme(get_best_approximation(exp(x), (0, 1), 6, 7, point=0.5))
generate_for_readme(get_best_approximation(ln(1 + x), (0, 1), 6, 20))
generate_for_readme(get_best_approximation(sin(x) / x, (-1, 1), 8, 18))
generate_for_readme(get_best_approximation(cos(x), (-1, 1), 8, 18))

print('## Functions\n')

for (function_name, function_link) in table_of_contents:
    print(f'* [`{function_name}`](#{function_link})')

print('\n')

for function_entry in function_entries:
    print(function_entry)
