from vehicle import Vehicle
from transports import Bicycle, NormalCar, SportsCar


class DrivingSimulator:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, new_vehicle):
        if isinstance(new_vehicle, Vehicle):
            self._vehicles.append(new_vehicle)
        else:
            print(f'{new_vehicle}은 교통 수단이 아니기 때문에 추가할 수 없습니다.')

    def start_all_vehicles(self):
        print('모든 교통 수단을 주행 시작시킵니다!')
        print()
        [vehicle.start() for vehicle in self._vehicles]

    def stop_all_vehicles(self):
        print('모든 교통 수단을 주행 정지시킵니다!')
        print()
        [vehicle.stop() for vehicle in self._vehicles]

    def __str__(self):
        return '\n'.join([str(vehicle) for vehicle in self._vehicles]) + '\n'


if __name__ == '__main__':
    # 자전거 인스턴스
    bicycle = Bicycle(0)

    # 일반 자동차 인스턴스들
    car_1 = NormalCar(0, 100)
    car_2 = NormalCar(0, 120)

    # 스포츠카 인스턴스들
    sports_car_1 = SportsCar(0, 200)
    sports_car_2 = SportsCar(0, 190)


    # 주행 시뮬레이터 인스턴스
    driving_simulator = DrivingSimulator()

    # 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
    driving_simulator.add_vehicle(bicycle)
    driving_simulator.add_vehicle(car_1)
    driving_simulator.add_vehicle(car_2)
    driving_simulator.add_vehicle(sports_car_1)
    driving_simulator.add_vehicle(sports_car_2)
    driving_simulator.add_vehicle(1)

    # 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
    driving_simulator.start_all_vehicles()
    print(driving_simulator)

    # 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
    driving_simulator.stop_all_vehicles()
    print(driving_simulator)