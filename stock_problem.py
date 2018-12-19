def solution1(prices):
    profit = 0
    buy_index = 0

    while True:
        while (buy_index + 1 < len(prices) and
               prices[buy_index] > prices[buy_index + 1]):
            buy_index += 1

        sell_index = buy_index + 1

        while (sell_index + 1 < len(prices) and
               prices[sell_index] < prices[sell_index + 1]):
            sell_index += 1

        if (sell_index >= len(prices)
                or buy_index >= len(prices)):
            break

        profit += prices[sell_index] - prices[buy_index]
        buy_index = sell_index + 1

    return profit


