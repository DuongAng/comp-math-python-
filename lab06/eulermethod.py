from prettytable import PrettyTable

from abstract import Abstract

#Pp euler
class MethodEuler(Abstract):

    name = "Euler method"
    p = 1

    def solved(self) -> [list[float], list[float]]:
        y, table, list_x, list_y = self.perform_method_euler()
        while True:
            self.h /= 2
            new_y, new_table, list_new_x, list_new_y = self.perform_method_euler()
            if abs(y - new_y) / (2 ** self.p - 1) <= self.e:
                print(table)
                return list_x, list_y
            y = new_y
            table = new_table
            list_x = list_new_x
            list_y = list_new_y

    def perform_method_euler(self) -> [float, PrettyTable, list[float], list[float]]:
        table = PrettyTable()
        table.title = self.name
        table.field_names = ["i", "xi", "yi", "f(xi, yi)", "Exact solution"]
        table.float_format = ".5"
        x = self.x0
        y = self.y0
        list_y = [y]
        list_x = [x]
        i = 0
        while x < self.x_n + self.h:
            table.add_row([i, x, y, self.f(x, y), self.f_as(x)])
            y += self.h * self.f(x, y)
            list_x.append(x)
            list_y.append(y)
            x += self.h
            i += 1
        return y, table, list_x, list_y
