"""
11. Container With Most Water
Medium

12820

818

Add to List

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
Accepted
1,175,657
Submissions
2,209,268
"""
from typing import List

class Solution:
    def maxArea_timelimitted(self, height: List[int]) -> int:
        import numpy as np
        length  = len(height)
        dis_arr = np.zeros((length, length))
        for i in range(length):
            for j in range(length-1,-1,-1):
                if i==j:
                    return int(dis_arr.max())

                if height[i]<height[j]: # 那其他的j就没有意义了，都不会更加大了
                    dis_arr[i,j] = height[i]*(j-i)
                    break
                elif height[i]>=height[j]:
                    dis_arr[i,j] = height[j]*(j-i)
    def maxArea_timelimitted_improve(self, height: List[int]) -> int:
        length  = len(height)
        MAX = 0
        for i in range(length):
            for j in range(length-1,-1,-1):
                if i==j:
                    return MAX

                if height[i]<height[j]: # 那其他的j就没有意义了，都不会更加大了
                    MAX = max(MAX,height[i]*(j-i))
                    break
                elif height[i]>=height[j]:
                    MAX = max(MAX, height[j]*(j-i))

    def maxArea(self, height: List[int]) -> int:
        MAX = 0
        x = len(height) - 1
        y = 0
        while x != y:
            if height[x] > height[y]:
                area = height[y] * (x - y)
                y += 1
            else:
                area = height[x] * (x - y)
                x -= 1
            MAX = max(MAX, area)
        return MAX



if __name__ == '__main__':
    So = Solution()
    print(So.maxArea([1,8,6,2,5,4,8,3,7]))
    """
    看了分析才写出来的：https://leetcode.com/problems/container-with-most-water/discuss/6099/Yet-another-way-to-see-what-happens-in-the-O(n)-algorithm
    但是我发现我写的for循环就超时了，用while就通过了：
    Success Details：
        Runtime: 944 ms, faster than 18.14% of Python3 online submissions for Container With Most Water.
        Memory Usage: 27.3 MB, less than 83.52% of Python3 online submissions for Container With Most Water.
    
    while比for快？？？improve之后还是超时。。

    """