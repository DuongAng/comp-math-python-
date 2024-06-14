from Equation import Equation


def ask_for_equations(equations_list: list[Equation]) -> [int, Equation]:
    while True:
        try:
            print("Select an equation:")
            print("\n".join(f"{i+1}) " + str(equations_list[i]) for i in range(len(equations_list))))
            i = int(input()) - 1
            if i == -1: # enter 0
                print("Please enter a number greater than 0")
                continue
            return i, equations_list[i]
        except ValueError:
            print("Faulty input")
        except IndexError:
            print("Please enter a number from 1 - 3")


def ask_float(questions: str) -> float:
    num: float
    while True:
        try:
            num = float(input(questions))
            return num
        except ValueError:
            print("Value must be a number")
