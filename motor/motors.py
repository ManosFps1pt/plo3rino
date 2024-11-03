from enum import Enum


class Motor(Enum):
    x: int = 0
    y: int = 1


if __name__ == '__main__':
    var = Motor.x
    print(var.value)
