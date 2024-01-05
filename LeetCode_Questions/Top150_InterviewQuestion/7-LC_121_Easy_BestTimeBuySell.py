"""     121.    Best Time to Buy and Sell Stock      Easy         

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4"""

testcases = [
    [1,3,7,4,6,11,10,17],
    [3,3,5,0,0,3,1,4],
    [1,2,3,4,5],
    [7,6,4,3,1],
    [3,2,6,5,0,3],
    [1,2,4,2,5,7,2,4,9,0],
    [2,1,4],
    [2,1,2,0,1],
    [7,1,5,3,6,4],
]

def maxProfit(prices: list[int]) -> int:

    # Time - 769ms beats 99%
    # Memory - 27.2MB beats 78%
    
    max_profit = 0
    min_buy = float('inf') # Buy
    
    for price in prices:    
        if price<min_buy:   # the ifs are to save time, max/min is slower
            min_buy = price

        elif price-min_buy > max_profit:
            max_profit = price-min_buy

        #profit = price-min_buy
        #min_buy = min(min_buy, price)
        #max_profit = max(max_profit, profit)

    return max_profit       


def maxProfit_knowDay(prices: list[int]) -> int:

    """The difference is:
        if I want to know the index of the best day to sell
        The Best Left and Right Point will kept saved in mem
    """

    maxprofit = 0

    lp = 0 # Buy
    minlp = float('inf')
    maxrp = 0 # Sell

    for i in range(1,len(prices)):
        profit = prices[i] - prices[lp]

        if prices[lp] > prices[i]:
            lp = i
        
        elif profit > maxprofit:
            minlp = lp
            maxrp = i
            maxprofit = prices[i] - prices[lp]      

    if maxprofit == 0:
        minlp, maxrp = 0, 0

    return maxprofit, minlp, maxrp

for test in testcases:
    print(maxProfit(test))

# for test in testcases:
#     print(maxProfit_knowDay(test))