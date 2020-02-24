class MyCustomList(list):
    
    def __getitem__(self, index):
        if index == 0:
            raise ValueError
        index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:
            raise ValueError
        index = index - 1
        return list.__setitem__(self, index, value)

    def __delitem__(self, key):
        key = key - 1
        return list.__delitem__(self, key)

    def __mul__(self, other):
        mul_list = [x * y for x, y in zip(self, other)]
        return MyCustomList(mul_list)


if __name__ == '__main__':
    list_one = MyCustomList([1, 2, 3, 4, 5])
    # print(list_one[0])  # raise value error
    print(list_one[1])

    list_one[1] = 100
    print(list_one)

    del list_one[1]
    print(list_one)

    list_one = MyCustomList([1, 2, 3, 4, 5])
    list_two = MyCustomList([2, 4, 6, 8, 10])
    list_three = list_one * list_two
    print(list_three)