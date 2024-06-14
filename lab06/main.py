import math

import numpy as np

from console import ask_for_equations, ask_float
from eulermethod import MethodEuler
from abstract import Abstract
from eulerModified import MethodEulerModified
from milnemethod import MethodMilne
from Equation import Equation

import matplotlib.pyplot as plt
#pt vi phân và nghiệm 
equation_lists: list[Equation] = [
    Equation(lambda x, y: x ** 2 - y, lambda x: x ** 2 - 2 * x + 2, "y' = x^2 - y"),
    Equation(lambda x, y: x ** 3 - y, lambda x: np.exp(-x) + x ** 3 - 3 * x ** 2 + 6 * x - 6, "y` = x^3 - y"),
    Equation(lambda x, y: 3 * x ** 2 - 2 * y, lambda x: np.exp(-2 * x) + 1.5 * x ** 2 - 0.75 * x + 0.375, "y' = 3x^2 - 2y"),
]

solvers_method: list[type[Abstract]] = [
    MethodEuler,
    MethodEulerModified,
    MethodMilne
]


def main():
    _, equation = ask_for_equations(equation_lists)
    x0 = ask_float("Enter x0 ")
    y0 = ask_float("Enter y0 ")
    x_n = ask_float("Enter x_n ")
    h = ask_float("Enter step h ")
    e = ask_float("Enter accuracy e ")
    print()
    for solver_class in solvers_method:
        solver = solver_class(x0, y0, x_n, h, e, equation.equations, equation.solve)
        list_x, list_y = solver.solved()
        plt.plot(list_x, list_y, label=solver.name)
    list_x = np.linspace(x0, x_n, 1000)
    plt.plot(list_x, equation.solve(list_x), label="Exact value")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
