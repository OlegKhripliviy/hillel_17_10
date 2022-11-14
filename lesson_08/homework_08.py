from abc import ABC, abstractmethod
from random import choice


class Shape(ABC):
    @abstractmethod
    def draw(self):
        """Return figure"""


class Rectangle(Shape):
    def draw(self):
        rectangle = " ---\n|  |\n ---"
        print(rectangle)


class Circle(Shape):
    def draw(self):
        circle = " -- \n-  -\n -- "
        print(circle)


def get_shape() -> Shape:
    options: list[Shape] = [Circle(), Rectangle()]
    return choice(options)


def main():
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
