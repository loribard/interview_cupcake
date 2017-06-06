stock_prices_yesterday = [10, 7, 5, 8, 11, 9]


def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError("Getting a profit requires at least 2 prices")
    max_profit = max(stock_prices_yesterday) - stock_prices_yesterday[0]
    for i in range(len(stock_prices_yesterday)-1):
        if max(stock_prices_yesterday[i+1:]) - stock_prices_yesterday[i] > max_profit:
            max_profit = max(stock_prices_yesterday[i+1:]) - stock_prices_yesterday[i]
    return max_profit


print get_max_profit(stock_prices_yesterday)
