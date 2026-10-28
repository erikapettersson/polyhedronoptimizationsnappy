
from sage.all import Polyhedron, MixedIntegerLinearProgram

def optimize_linear(inequalities, objective, maximize=True):
    P = Polyhedron(ieqs=inequalities)

    if P.is_empty():
        return {"status": "infeasible"}

    lp = MixedIntegerLinearProgram(maximization=maximize)
    variables = lp.new_variable(real=True)

    # Add the polyhedron's inequalities to the linear program.
    for row in inequalities:
        b = row[0]
        coeffs = row[1:]
        lp.add_constraint(
            sum(coeffs[i] * variables[i] for i in range(len(coeffs))),
            min=-b
        )

    expression = sum(
        objective[i] * variables[i]
        for i in range(len(objective))
    )

    lp.set_objective(expression)
    value = lp.solve()
    point = lp.get_values(variables)

    return {
        "status": "optimal",
        "objective_value": value,
        "point": [point[i] for i in range(len(objective))]
    }
