class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        self.fuel_tank = FuelTank(fuel)
        self.crew_manager = CrewManager(num_crew)
        self.supply_hold = SupplyHold(supplies, self.crew_manager)
        self.engine = Engine(self.fuel_tank, fuel_per_hour)


class FuelTank:
    """연료 탱크 클래스"""
    def __init__(self, fuel):
        """연료 탱크에 저장된 연료량을 인스턴스 변수로 갖는다"""
        self.fuel = fuel

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def use_fuel(self, amount):
        """연료 사용 메소드"""
        if self.fuel - amount >= 0:
            self.fuel -= amount
            return True
        print('연료가 부족합니다!')
        return False

    def report_fuel(self):
        """연료량 보고 메소드"""
        print(f'현재 연료는 {self.fuel}L 남아 있습니다')


class Engine:
    """엔진 클래스"""
    def __init__(self, fuel_tank, fuel_per_hour):
        """연료 탱크 인스턴스와 시간당 연료 소비량을 인스턴스 변수로 갖는다"""
        self.fuel_tank = fuel_tank
        self.fuel_per_hour = fuel_per_hour

    def run_for_hours(self, hours):
        """엔진 작동 메소드, 연료 탱크 인스턴스를 사용한다"""
        if self.fuel_tank.use_fuel(self.fuel_per_hour * hours):
            print(f'엔진을 {hours}시간 동안 돌립니다!')
            return True
        print('엔진이 부족하기 때문에 엔진작동을 시작할 수 없습니다')
        return False


class CrewManager:
    """선원 관리 클래스"""
    def __init__(self, num_crew):
        """승선한 선원 수를 인스턴스 변수로 갖는다"""
        self.num_crew = num_crew

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def report_crew(self):
        """선원 수 보고 메소드"""
        print(f'현재 선원 {self.num_crew}명이 있습니다')


class SupplyHold:
    """물자 창고 클래스"""
    def __init__(self, supplies, crew_manager):
        """물자량과 선원 관리 인스턴스를 인스턴스 변수로 갖는다"""
        self.supplies = supplies
        self.crew_manager = crew_manager

    def load_supplies(self, amount):
        """물자 충전 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드, 각 선원들에게 동일한 양의 물자를 배분한다"""
        if self.supplies >= self.crew_manager.num_crew:
            self.supplies -= self.crew_manager.num_crew
            return True
        print('물자가 부족하기 때문에 배분할 수 없습니다')
        return False

    def report_supplies(self):
        """물자량 보고 메소드"""
        print(f'현재 물자는 {self.supplies}명분이 남아 있습니다.')


if __name__ == '__main__':
    ship = Ship(400, 10, 1000, 50)
    
    # 다른 클래스에 전가된 책임을 통해 동작
    ship.fuel_tank.load_fuel(10)
    ship.supply_hold.load_supplies(10)
    ship.crew_manager.load_crew(10)

    ship.supply_hold.distribute_supplies_to_crew()
    ship.engine.run_for_hours(4)

    ship.fuel_tank.report_fuel()
    ship.supply_hold.report_supplies()
    ship.crew_manager.report_crew()
    