"""
121. Best Time to Buy and Sell Stock
Easy

12153

447

Add to List

Share
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

1 <= prices.length <= 105
0 <= prices[i] <= 104
Accepted
1,684,239
Submissions
3,174,734
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices)<2:
            return 0
        curr_profit = 0
        for i in range(1, len(prices)):
            curr_profit = max(0, curr_profit+prices[i]-prices[i-1])
            max_profit = max(max_profit, curr_profit)

        return max_profit





if __name__ == '__main__':
    So = Solution()
    print(So.maxProfit([7,1,5,3,6,4]))
    """
    Success Details: 
        Runtime: 1652 ms, faster than 8.61% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 25.1 MB, less than 83.31% of Python3 online submissions for Best Time to Buy and Sell Stock.
    
    很慢，但是省内存倒是
    """