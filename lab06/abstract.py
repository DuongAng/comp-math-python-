from typing import Callable

#Định nghĩa các method 

class Abstract:
    name = ""
    def __init__(self,
                 x0: float,
                 y0: float,
                 x_n: float,
                 h: float,
                 e: float,
                 f: Callable[[float, float], float],
                 f_as: Callable[[float], float]):
        self.x0 = x0
        self.y0 = y0
        self.x_n = x_n
        self.h = h
        self.e = e
        self.f = f
        self.f_as = f_as

    def solved(self) -> list[float]:
        raise NotImplementedError()
