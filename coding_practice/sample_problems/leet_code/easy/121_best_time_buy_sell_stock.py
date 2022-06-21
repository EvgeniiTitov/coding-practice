from typing import List


'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''


class Solution:

    # Brute force - time limit exceeded, T: O(n2); S: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        for i in range(length):
            for j in range(i + 1, length):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit

    # Single pass - T: O(n), S: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        '''
        The points of interest are the peaks and valleys in the given graph. 
        We need to find the largest peak following the smallest valley. 
        We can maintain two variables - minprice and maxprofit corresponding 
        to the smallest valley and maximum profit (maximum difference between 
        selling price and minprice) obtained so far respectively.
        '''
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        left, right = 0, 1
        max_profit = 0
        while right < length:
            buy_price = prices[left]
            sell_price = prices[right]
            temp_profit = sell_price - buy_price

            if buy_price < sell_price:
                max_profit = max(max_profit, temp_profit)
            else:
                left = right

            right += 1
        return max_profit
