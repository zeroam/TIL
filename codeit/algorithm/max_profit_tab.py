def max_profit_tab(price_list, count):
    profit_table = [0]

    for i in range(1, count + 1):
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])
        profit_table.append(profit)

    return profit


if __name__ == '__main__':
    result = max_profit_tab([0, 200, 600, 900, 1200, 2000], 5)
    print(result)
    assert result == 2000

    result = max_profit_tab([0, 300, 600, 700, 1100, 1400], 8)
    print(result)
    assert result == 2400

    result = max_profit_tab([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9)
    print(result)
    assert result == 1800