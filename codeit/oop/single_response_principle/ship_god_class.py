class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        """
        :param fuel: 연료량
        :param fuel_per_hour: 시간당 연료 소비량
        :param supplies: 물자량
        :param num_crew: 선원 수
        """
        self.fuel = fuel
        self.fuel_per_hour = fuel_per_hour
        self.supplies = supplies
        self.num_crew = num_crew

    def report_fuel(self):
        """연료량 보고 메소드"""
        print(f"현재 연료는 {self.fuel}L 남아 있습니다")

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def report_supplies(self):
        """물자량 보고 메소드"""
        print(f'현재 물자는 {self.supplies}명분이 남아 있습니다')

    def load_supplies(self, amount):
        """물자 보급 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드"""
        if self.supplies >= self.num_crew:
            self.supplies -= self.num_crew
            return True
        print('물자가 부족하기 때문에 배분할 수 없습니다')
        print(False)

    def report_crew(self):
        """선원 수 보고 메소드"""
        print(f'현재 선원 {self.num_crew}명이 있습니다')


    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def run_engine_for_hours(self, hours):
        """엔진 작동 메소드"""
        if self.fuel > self.fuel_per_hour * hours:
            self.fuel -= self.fuel_per_hour * hours
            print(f'엔진을 {hours}시간 동안 돌립니다!')
        else:
            print('연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다')


if __name__ == '__main__':
    # 하나의 클래스에 너무 많은 책임 (연료, 물자, 선원, 엔진)
    ship = Ship(400, 10, 1000, 50)
    
    ship.load_fuel(10)
    ship.load_supplies(10)
    ship.load_crew(10)

    ship.distribute_supplies_to_crew()
    ship.run_engine_for_hours(4)

    ship.report_fuel()
    ship.report_supplies()
    ship.report_crew()
    