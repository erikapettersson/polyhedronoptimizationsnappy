/content/polyhedronoptimizationsnappy

from sage.all import Polyhedron, MixedIntegerLinearProgram


def optimize_linear(inequalities, objective, maximize=True):
    """Optimize a linear objective over a polyhedron.

    Each inequality (b, a1, a2, ...) means:
        b + a1*x1 + a2*x2 + ... >= 0
    """
    P = Polyhedron(ieqs=inequalities)

    if P.is_empty():
        return {"status": "infeasible"}

    dimension = len(objective)

    if any(len(row) != dimension + 1 for row in inequalities):
        raise ValueError(
            "Each inequality must have one constant plus one coefficient per variable."
        )

    lp = MixedIntegerLinearProgram(maximization=maximize)
    variables = lp.new_variable(real=True)

    for row in inequalities:
        b = row[0]
        coeffs = row[1:]

        lp.add_constraint(
            sum(coeffs[i] * variables[i] for i in range(dimension)),
            min=-b,
        )

    expression = sum(
        objective[i] * variables[i]
        for i in range(dimension)
    )

    lp.set_objective(expression)

    value = lp.solve()
    point = lp.get_values(variables)

    return {
        "status": "optimal",
        "objective_value": value,
        "point": [point[i] for i in range(dimension)],
    }
