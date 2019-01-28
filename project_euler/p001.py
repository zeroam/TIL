def multiple(num):
    answer = 0
    for i in range(num):
        if i%3 == 0 or i%5 == 0:
            answer += i
    return answer

if __name__ == "__main__":
    print(multiple(1000))