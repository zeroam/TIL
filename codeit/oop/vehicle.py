from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @property
    @abstractmethod
    def speed(self):
        pass

    def stop(self):
        self.speed = 0


if __name__ == '__main__':
    print(Vehicle.mro())
    print(dir(Vehicle))
