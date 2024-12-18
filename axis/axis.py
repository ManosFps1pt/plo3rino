from enum import Enum


class Axis(Enum):
    x: int = 0
    y: int = 1


if __name__ == '__main__':
    var = Axis.x
    print(var.value)
