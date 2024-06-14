from prettytable import PrettyTable

from abstract import Abstract


class MethodMilne(Abstract):

    name = "Milne method"
    p=4
    
    def solved(self) -> [list[float], list[float]]:
        while True:
            max_eps, table, list_x, list_y = self.perform_method_milne()
            self.h /= 2
            print(max_eps)
            if max_eps <= self.e:
                print(table)
                return list_x, list_y

    def perform_method_milne(self) -> [float, PrettyTable, list[float], list[float]]:
        table = PrettyTable()
        table.title = self.name
        table.field_names = ["i", "xi", "yi", "f(xi, yi)", "Exact solution", "e"]
        table.float_format = ".5"
        max_eps = 0.0
        x = self.x0
        f = self.f
        h = self.h
        y = self.y0
        list_x = [x]
        list_y = [y]
        list_f = [f(x, y)]
        for i in range(3):
            k1 = h * f(x, y)
            k2 = h * f(x + h / 2.0, y + k1 / 2.0)
            k3 = h * f(x + h / 2.0, y + k2 / 2.0)
            k4 = h * f(x + h, y + k3)
            y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            list_f.append(f(x, y))
            list_x.append(x)
            list_y.append(y)
            x += h
        i = 0
        while x < self.x_n + self.h:
            y = list_y[-4] + 4 * h / 3 * (2 * list_f[-3] - list_f[-2] + 2 * list_f[-1])
            new_corrected_y = list_y[-2] + h / 3 * (list_f[-2] + 4 * list_f[-1] + self.f(x, y))
            table.add_row([i + 3, x, new_corrected_y, self.f(x, y), self.f_as(x), abs(y - self.f_as(x))])
            while abs(y - new_corrected_y) > self.e:
                y = new_corrected_y
                new_corrected_y = list_y[-2] + h / 3 * (list_f[-2] + 4 * list_f[-1] + self.f(x, y))
                table.add_row(["", "", new_corrected_y, self.f(x, y), self.f_as(x), abs(new_corrected_y - self.f_as(x))])
            y = new_corrected_y
            list_x.append(x)
            list_y.append(y)
            list_f.append(self.f(x, y))
            max_eps = max(max_eps, abs(y - self.f_as(x)))
            y += self.h * self.f(x, y)
            x += self.h
            i += 1
        return max_eps, table, list_x, list_y
