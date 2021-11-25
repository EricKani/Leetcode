"""
119. Pascal's Triangle II
Easy

1975

246

Add to List

Share
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

Accepted
443,220
Submissions
800,877
"""
from typing import List

class Solution:
    def getRow_from118(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        dp = [[1], [1, 1]]
        if numRows in [1, 2]:
            return dp[rowIndex]
        for k in range(3, numRows + 1):
            dp.append([i + j for i, j in zip([0] + dp[k - 2], dp[k - 2] + [0])])
        return dp[rowIndex]

    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1],[1,1]]
        if rowIndex in [0,1]:
            return dp[rowIndex]

        for k in range(2, rowIndex + 1):
            dp.append([i + j for i, j in zip([0] + dp[-1], dp[-1] + [0])])
            dp.pop(0)
        return dp[-1]


if __name__ == '__main__':
    So = Solution()
    print(So.getRow(5))

    """
    Success Details: 
        Runtime: 39 ms, faster than 22.80% of Python3 online submissions for Pascal's Triangle II.
        Memory Usage: 14.2 MB, less than 53.26% of Python3 online submissions for Pascal's Triangle II.
    
    直接118的方法就能通过这道题。不太对，有什么高效手段吗？？
    去除前边元素的操作，只会降低效率，并不会降低memory。。日 先这么地吧
    
    """
