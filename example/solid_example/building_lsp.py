class Building:
    material = '건물재료'
    def __init__(self, name):
        self.name = name

    def build(self):
        print(f'{self.material}으로 {self.name}을 짓습니다.')


class ConcreteBuilding(Building):
    material = '콘크리트'

    def mold(self):
        print('건물 몰딩을 합니다.')


if __name__ == '__main__':
    building_1 = Building('건물1')
    building_2 = Building('건물2')
    concrete_building = ConcreteBuilding('콘크리트건물')

    building_list = []
    building_list.append(building_1)
    building_list.append(building_2)
    building_list.append(concrete_building)

    for building in building_list:
        building.build()
