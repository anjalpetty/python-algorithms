"""
Leetcode: 121: Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
"""


def max_profit(prices):
  buy = prices[0]
  profit = 0

  for i in range(1, len(prices)):
    if prices[i] < buy:
      buy = prices[i]
      continue
    cur_profit = prices[i] - buy
    profit = max(cur_profit, profit)
  return profit


if __name__ == '__main__':
  print(max_profit([7, 1, 5, 3, 6, 4]))  # expects 5
  print(max_profit([7, 6, 4, 3, 1]))  # expects 0
