def max_profit_memo(price_list, count, cache):
    # base case
    if count in [0, 1]:
        return price_list[count]
        
    if count in cache:
        return cache[count]
    
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0
    
    # recursive case
    for i in range(1, count // 2 + 1):
        profit = max(profit,
            max_profit_memo(price_list, i , cache) +
            max_profit_memo(price_list, count - i, cache))
    cache[count] = profit
    
    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


if __name__ == '__main__':
    count = 10
    for i in range(count):
        price_list = [0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200]
        my_result = max_profit(price_list, i)
        print(f'{i}th result: {my_result}')