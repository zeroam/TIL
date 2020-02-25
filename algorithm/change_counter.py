# 1센트, 5센트, 10센트, 25센트, 50센트 동전이 있고
# 동전을 무한정 확보할 수 있다고 하면
# 이들의 조합으로 특정 금액 m을 만들 수 있는 경우의 수는?
class ChangeCounter:

    def __init__(self, coins):
        self._coins = coins

    @property
    def coins(self):
        return self._coins

    def _count_recursive(self, amount, index):
        if amount == 0:
            return 1
        elif (amount < 0 or index >= len(self._coins)):
            return 0
        else:
            return self._count_recursive(amount - self._coins[index], index) \
                 + self._count_recursive(amount, index + 1)

    def __call__(self, amount):
        return self._count_recursive(amount, 0)

    
if __name__ == '__main__':
    counter = ChangeCounter([50, 25, 10, 5, 1])
    print(counter(5))