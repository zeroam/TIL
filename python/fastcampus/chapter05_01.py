# copy vs deepcopy
class Baseket(object):
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Baseket(["Apple", "Bag", "TV", "Snack", "Water"])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print(id(basket1), id(basket2), id(basket3))
print(id(basket1._products), id(basket2._products), id(basket3._products))
print()

basket1.put_prod("Orange")
basket2.del_prod("Snack")

print(basket1._products)
print(basket2._products)
print(basket3._products)
print()


# 함수 매개변수 전달 사용법
def add(x, y):
    x += y
    return x


x = 10
y = 5
print(add(x, y), x, y)

a = [10, 15]
b = [5, 20]
print(add(a, b), a, b)  # 가변형 a -> 데이터 변경

c = (10, 15)
d = (5, 20)
print(add(c, d), c, d)  # 불변형 a -> 원본데이터 변경 안됨
print()


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple: 사본 생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print(tt1 is tt2, id(tt1), id(tt2))
print(tt1 is tt3, id(tt1), id(tt3))

# 인터프리터에서 테스트할 때는 다르게 나옴
tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
print(tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))

ss1 = "Apple"
ss2 = "Apple"
print(ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
