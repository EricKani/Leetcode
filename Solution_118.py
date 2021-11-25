"""
118. Pascal's Triangle
Easy

4126

176

Add to List

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
Accepted
635,645
Submissions
1,044,294
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1],[1,1]]
        if numRows in [1,2]:
            return dp[:numRows]
        for k in range(3, numRows+1):
            dp.append([i+j for i,j in zip([0]+dp[k-2], dp[k-2]+[0])])
        return dp





if __name__ == '__main__':
    So = Solution()
    print(So.generate(5))
    """
    Success Details: 
        Runtime: 28 ms, faster than 86.92% of Python3 online submissions for Pascal's Triangle.
        Memory Usage: 14.2 MB, less than 57.93% of Python3 online submissions for Pascal's Triangle.
    
    比较简单：错位相加
    目前理解：
        1）动态规划是遍历一遍，
        2）找两个初始简单结果为基础，遍历过程中生成中间结果。
    """