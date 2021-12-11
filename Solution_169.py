"""
169. Majority Element
Easy

7158

297

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1


Follow-up: Could you solve the problem in linear time and in O(1) space?
Accepted
1,008,117
Submissions
1,637,027
"""

from typing import List

class Solution:
    def majorityElement_liumang(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0

        for num in nums:
            if candidate == num:
                count += 1
            elif count==0:
                candidate, count = num, 1
            else:
                count-=1

        return candidate

    def majorityElement_sort(self, nums: List[int]) -> int:
        self.fast_sort(nums, 0, len(nums)-1)
        print(nums)
        return nums[len(nums) // 2]

    def fast_sort(self, li, start, end):
        if start>=end:
            return
        mid = li[start]
        low = start
        high = end

        while low < high:
            while low < high and li[high] >= mid:
                high-=1
            li[low] = li[high]

            while low < high and li[low]< mid:
                low+=1
            li[high] = li[low]

        li[low] = mid

        self.fast_sort(li, start, low-1)
        self.fast_sort(li, low+1, end)



if __name__ == '__main__':
    so = Solution()
    print(so.majorityElement([4,43,4,5,2,3,4,3,1]))

    """
    最流氓写法，直接用python的内置sort。太tm方便了,效率也很ok，但你知道这不是你想要的。
    Success Details: 
        Runtime: 160 ms, faster than 88.95% of Python3 online submissions for Majority Element.
        Memory Usage: 15.5 MB, less than 54.34% of Python3 online submissions for Majority Element.
    --------------------------------------------------------
    自己实现: 快速排序是基于二分的思想（基本抄的）
    超时了
    --------------------------------------------------------
    直观实现：是针对这个问题设计的解决思路，过半；不是很好想。
    Success Details:    
        Runtime: 156 ms, faster than 95.02% of Python3 online submissions for Majority Element.
        Memory Usage: 15.5 MB, less than 54.35% of Python3 online submissions for Majority Element.
    
    """