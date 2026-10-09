
from abc import ABC, abstractmethod
from typing import List
import math


# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""
        pass

    def describe(self) -> str:
        """Return the shape's name and area formatted to two decimal places."""
        return f"{self.__class__.__name__}: Area = {self.area():.2f}"


# Circle class
class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


# Triangle class
class Triangle(Shape):

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


# Function to render shapes
def render_shapes(shapes: List[Shape]) -> List[str]:
    descriptions = []

    for shape in shapes:
        descriptions.append(shape.describe())

    return descriptions


# Main program
if __name__ == "__main__":

    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Triangle(8.0, 3.0)
    ]

    results = render_shapes(shapes)

    for description in results:
        print(description)