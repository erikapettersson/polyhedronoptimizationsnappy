
from sage.all import Polyhedron


def optimize_linear(inequalities, objective, maximize=True):
    """Optimize a linear objective over a polyhedron.

    Each inequality (b, a1, a2, ...) means
    b + a1*x1 + a2*x2 + ... >= 0.
    """
    P = Polyhedron(ieqs=inequalities)

    if P.is_empty():
        return {"status": "infeasible"}

    lp, variables = P.to_linear_program(return_variable=True)

    if len(objective) != len(variables):
        raise ValueError("Objective dimension does not match polyhedron.")

    expression = sum(
        objective[i] * variables[i]
        for i in range(len(objective))
    )

    lp.set_objective(expression)

    # Set the direction using the API supported by your installation.
    lp.set_maximization() if maximize else lp.set_minimization()

    value = lp.solve()
    point = lp.get_values(*variables)

    return {
        "status": "optimal",
        "objective_value": value,
        "point": point,
    }
