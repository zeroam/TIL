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


class Square(Rectangle):
    """정사각형 클래스"""

    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1


if __name__ == '__main__':
    rectangle_1 = Rectangle(4, 6)
    rectangle_2 = Square(2)

    rectangle_1.width = 3
    rectangle_1.height = 7

    print(rectangle_1.area())

    # 부모 클래스의 인스턴스를 사용하는 위치에
    # 자식 클래스의 인스턴스를 대신 사용했을 때
    # 코드가 원래 의도대로 작동해야 한다
    rectangle_2.width = 3
    rectangle_2.height = 7

    print(rectangle_2.area())
