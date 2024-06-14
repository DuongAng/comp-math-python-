import math


class WrongData(Exception):
    pass


class NewtonInterpolatorcaculator:
    @staticmethod
    def interpolate_divided_difference(x_values, y_values, x):
        raise WrongData("This program can't interpolate by Newton polynom with divided difference.")

    #Tính toán hiệu chệnh lệch bậc \delta
    @staticmethod
    def delta(values, value_pos, power):
        if power == 0:
            return values[value_pos]
        else:
            return NewtonInterpolatorcaculator.delta(values, value_pos + 1, power - 1) \
                   - NewtonInterpolatorcaculator.delta(values, value_pos, power - 1)

    @staticmethod
    def calculate_d(values, power):
        if power > len(values) + 1:
            return {'possible': False, 'difference': []}

        size = len(values)
        difference = [[' '] * size for arr in range(size)]

        for i in range(size):
            difference[i][0] = values[i]

        for j in range(1, size):
            for i in range(size - j):
                difference[i][j] = difference[i + 1][j - 1] - difference[i][j - 1]

        return {'possible': True, 'difference': difference}

    @staticmethod
    def get_t(t0, power, direct=True):
        answer = 1
        if power == 0:
            return answer
        else:
            if direct:
                for i in range(1, power + 1):
                    answer *= t0 - i + 1
                return answer
            else:
                for i in range(power, 0, -1):
                    answer *= t0 + i - 1
                return answer

    @staticmethod
    def direct_interpolation(x_values, y_values, x):
        n = len(x_values)
        h = x_values[1] - x_values[0]
        t = (x - x_values[0]) / h

        d = NewtonInterpolatorcaculator.calculate_d(y_values, n)
        if not d['possible']:
            raise WrongData
        difference = d['difference']

        answer = y_values[0]

        for power in range(1, n):  # if len(x_arr) == 7, -> i ... 6
            answer += NewtonInterpolatorcaculator.get_t(t, power, direct=True) \
                      * difference[0][power] \
                      / math.factorial(power)

        return answer

    @staticmethod
    def direct_interpolation_accurate(x_values, y_values, x):
        index_of_x_before = 0
        for i in range(len(x_values)):
            if x >= x_values[i]:
                index_of_x_before = i
            else:
                break

        n = len(x_values)
        h = x_values[1] - x_values[0]
        t = (x - x_values[index_of_x_before]) / h

        d = NewtonInterpolatorcaculator.calculate_d(y_values, n)
        if not d['possible']:
            raise WrongData
        difference = d['difference']
        print("Got difference:")
        from pandas import DataFrame
        print(DataFrame(difference))

        answer = y_values[index_of_x_before]
        print("N" + str(n - index_of_x_before) + " = " + str(answer), end='')
        for power in range(1, n - index_of_x_before):  # if len(x_arr) == 7, -> i ... 6
            answer += NewtonInterpolatorcaculator.get_t(t, power, direct=True) \
                      * difference[index_of_x_before][power] \
                      / math.factorial(power)
            print("  +  " + str(round(NewtonInterpolatorcaculator.get_t(t, power, direct=True), 3)) + " * " + str(round(difference[index_of_x_before][power], 3)) + " / " + str(math.factorial(power)), end="")
        print()
        return answer

    @staticmethod
    def back_interpolation(x_values, y_values, x):
        h = x_values[1] - x_values[0]
        n = len(x_values)
        t = (x - x_values[n - 1]) / h

        answer = NewtonInterpolatorcaculator.delta(y_values, n - 1, 0)
        for i in range(1, n):
            answer += NewtonInterpolatorcaculator.get_t(t, i, direct=False) \
                      * NewtonInterpolatorcaculator.delta(y_values, n - i - 1, i) \
                      / math.factorial(i)
        return answer

    @staticmethod
    def interpolate_finite_difference(x_values, y_values, x):
        mid_index = len(x_values) // 2
        mid = x_values[mid_index]
        if x < mid:
            return NewtonInterpolatorcaculator.direct_interpolation(x_values, y_values, x)
        else:
            return NewtonInterpolatorcaculator.back_interpolation(x_values, y_values, x)

    @staticmethod
    def interpolate(x_values, y_values, x):
        if not (x_values[0] <= x <= x_values[len(x_values) - 1]):
            raise WrongData("This progwam cannot extwapolate -_-")

        if len(x_values) < 2:
            raise WrongData("Not enough data please enter more")

        return NewtonInterpolatorcaculator.interpolate_finite_difference(x_values, y_values, x)

    @staticmethod
    def calculate_interpolations(x_values, y_values, interpolation_nodes):
        interpolated_y_values = []
        for i in range(len(interpolation_nodes)):
            interpolated_y = NewtonInterpolatorcaculator.interpolate(x_values, y_values, interpolation_nodes[i])
            interpolated_y_values.append(interpolated_y)
        return interpolated_y_values
