def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit



def maxProfit_cumulative(prices: list[int]) -> int:
    result = 0
    if len(prices) < 2:
        return result

    lowest = prices[0]
    for i in range(1, len(prices)):
        current = prices[i]

        # capture any gains immediately
        # by selling and then buying at the same price of prices[i]
        if current > lowest:
            result += (current - lowest)

        # otherwise, current <= lowest
        # if current == lowest: no harm updating without adding to result
        # if current < lowest: should update lowest to get max profit later on

        # simulates buying at current price (if we sell later)
        # or not buying at all (since no adding to result)
        lowest = current

    return result

prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("cumulative profit", maxProfit_cumulative(prices))
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("cumulative profit", maxProfit_cumulative(prices))
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("cumulative profit", maxProfit_cumulative(prices))
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""