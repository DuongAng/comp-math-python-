import LagrangeInterpolatorcaculator
from read_values_from_file import read_file
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

from LagrangeInterpolatorcaculator import LagrangeInterpolatorcaculator
from NewtonInterpolatorcaculator import NewtonInterpolatorcaculator
from NewtonInterpolatorcaculator import WrongData


def read_data():
    answer = input("Enter data:\n (1) Read from file \n (2) Read from the keyboard\n")
    if answer == "1":
        file_path = input("Enter file path:\n ")
        return read_file(file_path)
    elif answer == "2":
        x_values, y_values = [], []
        n = int(input("Enter number of points:\n "))
        print("Enter " + str(n) + " points like this x_i y_i: ")
        for i in range(n):
            line = input("x" + str(i) + " y" + str(i) + ": ")
            x_values.append(float(line.split()[0]))
            y_values.append(float(line.split()[1]))
        return {'x_arr': x_values, 'y_arr': y_values}
    else:
        raise ValueError


def lab05():
    x_arr, y_arr = [], []
    try:
        data = read_data()
        x_arr = data['x_arr']
        y_arr = data['y_arr']
    except (ValueError, TypeError) as some_error:
        print("Wrong input type. Please restart program!")
        return
    except FileNotFoundError:
        print("File not found. Please restart program!")
        return

    print("\nData Enter:")
    print(DataFrame({'x': x_arr, 'y': y_arr}))

    x = float(input("Enter x:\n>>> "))
    if x < x_arr[0] or x > x_arr[len(x_arr) - 1]:
        print("Sorry please enter x in range [x_min, x_max]")
        return

    # Lagrange
    interpolated_y = LagrangeInterpolatorcaculator.interpolate(x_arr, y_arr, x)
    print("Lagrange-interpolated y for x = " + str(x) + ":", interpolated_y)

    large_x_arr = np.linspace(x_arr[0], x_arr[len(x_arr) - 1], len(x_arr) * 10)
    interpolated_y_arr = LagrangeInterpolatorcaculator.calculate_interpolations(x_arr, y_arr, large_x_arr)
    # vẽ đồ thị
    plt.title("Lagrange polynom interpolation")
    plt.plot(x_arr, y_arr, 'bo') # các điểm xanh làm hình tròn
    plt.plot(large_x_arr, interpolated_y_arr, 'r') # đường màu đỏ 
    plt.plot([x], [interpolated_y], 'go') # điểm xanh lá cây tròn
    plt.show()

    # Newton
    try:
        interpolated_y = NewtonInterpolatorcaculator.interpolate(x_arr, y_arr, x)
        print("Newton-interpolated y for x = " + str(x) + ":", interpolated_y)

        large_x_arr = np.linspace(x_arr[0], x_arr[len(x_arr) - 1], len(x_arr) * 10)
        interpolated_y_arr = NewtonInterpolatorcaculator.calculate_interpolations(x_arr, y_arr, large_x_arr)
        #vẽ như trên
        plt.title("Newton polynom interpolation")
        plt.plot(x_arr, y_arr, 'bo')
        plt.plot(large_x_arr, interpolated_y_arr, 'r')
        plt.plot([x], [interpolated_y], 'go')
        plt.show()
    except WrongData as wrong_data_error:
        print(wrong_data_error.args[0])


if __name__ == '__main__':
    lab05()
