# polyopt

A Python package for optimizing linear objective functions over feasible polyhedra using Passagemath.

## Current features

- Define a feasible polyhedron using linear inequalities.
- Optimize a linear objective over the feasible region.
- Return an objective value and a candidate solution point.

## Installation

Install Passagemath in Google Colab:

    %pip install passagemath-standard

Install the package from its project directory:

    %pip install -e /content/polyopt

## Example

    from polyopt import optimize_linear

    constraints = [
        (0, 1, 0),
        (0, 0, 1),
        (4, -1, -1),
        (2, -1, 0),
        (3, 0, -1),
    ]

    result = optimize_linear(
        constraints,
        objective=[3, 2],
        maximize=True,
    )

    print(result)

## Development status

Early prototype. Improved error handling, input validation,
and automated tests are planned.

## Roadmap

- Improve solver-status handling.
- Add automated tests.
- Explore nonlinear objective functions.
