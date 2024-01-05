"""   122.   Best Time to Buy and Sell Stock II      Medium      

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4"""


""" My Notes 
The idea is sum all possible profits,

beacuse of this propriety:

prices = [7,1,3,5,2,4,8]

buy on day 2, sell on day 3, buy on day 3 sell in day 4:
3 - 1 = 2 and 5 - 3 = 2 -> 2 + 2 = 4 (profit)

is the same that buy on day 2 and sell in day 4
5 - 1 = 4

sum all possible profits until the left pointer move again."""

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

def maxProfit_while(prices: list[int]) -> int:
    maxprofit = 0
    lp = 0
    rp = 1

    while rp < len(prices):
        if prices[rp] > prices[lp]:
            maxprofit += prices[rp] - prices[lp]
        lp = rp
        rp += 1

    return maxprofit

# Change While by For

def maxProfit_for(prices: list[int]) -> int:
    maxprofit = 0
    buy = float('inf')

    for price in prices:
        if price < buy:
            buy = price

        else:
            maxprofit += price-buy
            buy = price

    return maxprofit


for test in testcases:
    print(maxProfit_for(test))