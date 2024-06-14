from dataclasses import dataclass
from typing import Callable

#Biểu diễn phương trình

@dataclass
class Equation:
    equations: Callable[[float, float], float]
    solve: Callable[[float], float]
    equation_strings: str

    def __str__(self) -> str:
        return self.equation_strings

    def __repr__(self) -> str:
        return self.equation_strings
