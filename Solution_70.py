"""
70. Climbing Stairs
Easy

9134

276

Add to List

Share
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
Accepted
1,248,867
Submissions
2,489,381
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        step = [1,2]
        for i in range(2,n):
            step.append(step[i-1]+step[i-2])
        return step[n-1]




if __name__ == '__main__':
    So = Solution()
    print(So.climbStairs(4))

    """
    Success Details: 
        Runtime: 30 ms, faster than 62.68% of Python3 online submissions for Climbing Stairs.
        Memory Usage: 14.3 MB, less than 11.87% of Python3 online submissions for Climbing Stairs.

    子问题选好会好想很多。不要陷入子问题，抽象出来
    另外这个runtime不是很准，不要太在意，memory usage确实是准确的
    """