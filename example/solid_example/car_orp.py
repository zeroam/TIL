from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.tire = None

    def set_tire(self, tire):
        self.tire = tire

    def run(self):
        if isinstance(self.tire, Tire):
            self.tire.run()
        else:
            print('타이어가 없습니다.')


class Tire(ABC):
    @abstractmethod
    def run(self):
        pass


class ATire(Tire):
    def __init__(self):
        self.durability = 5

    def run(self):
        if self.durability > 0:
            print(f'{self.__class__.__name__} 달립니다. 내구도: {self.durability}')
        else:
            print(f'{self.__class__.__name__} 내구도가 없습니다.')
        self.durability -= 1


class BTire(Tire):
    def __init__(self):
        self.durability = 10

    def run(self):
        if self.durability > 0:
            print(f'{self.__class__.__name__} 달립니다. 내구도: {self.durability}')
        else:
            print(f'{self.__class__.__name__} 내구도가 없습니다.')
        self.durability -= 1


if __name__ == '__main__':
    car = Car()
    a_tire = ATire()
    b_tire = BTire()

    car.set_tire(a_tire)
    for i in range(6):
        car.run()

    car.set_tire(b_tire)
    car.run()
