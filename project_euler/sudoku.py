# create sudoku puzzle
from random import randint
from pprint import pprint

n = 5

def nums_generate(n):
    num_list = [x for x in range(1,n+1)]
    result = []
    for i in range(n):
        result.append(num_list.pop(randint(0, len(num_list)-1)))
    return result

def array_generate(n):
    result = []
    for i in range(n):
        result.append(nums_generate(n))
    return result

result = array_generate(n)

count = 0
while True:
    flag = True
    for i in range(n):
        for j in range(n):
            for k in range(i):
               if result[i][j] == result[k][j]:
                   temp = result[i][j]
                   result[i].remove(temp)
                   result[i].append(temp)
                   flag = False
                   count += 1
                   if(count >= 100):
                       result = array_generate(n)
                       count = 0
    if(flag):
        break

pprint(result)
            