class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value if value > 0 else 1

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value if value > 0 else 1


class Square:
    """정사각형 클래스
    직사각형의 행동 규약을 지키기 어려움
    -> 상속 X"""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value if value > 0 else 1


if __name__ == '__main__':
    rectangle_1 = Rectangle(4, 6)
    square = Square(2)

    rectangle_1.width = 3
    rectangle_1.height = 7

    print(rectangle_1.area())

    square.side = 7

    print(square.area())
