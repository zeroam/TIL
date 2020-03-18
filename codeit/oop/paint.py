from math import pi, sqrt
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        print('도형의 넓이 계산 중!')

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        super().area()
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height


class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        return 3 * self.side


class Paint:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print('넓이, 둘레를 구하는 메소드가 없는 도형입니다')

    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes])


if __name__ == '__main__':
    triangle = EquilateralTriangle(4)
    circle = Circle(5)
    rectangle = Rectangle(5, 8)
    cylinder = Cylinder(3, 7)

    paint_program = Paint()
    paint_program.add_shape(triangle)
    paint_program.add_shape(circle)
    paint_program.add_shape(cylinder)
    paint_program.add_shape(rectangle)

    print(paint_program.total_area_of_shapes())
    print(paint_program.total_perimeter_of_shapes())
