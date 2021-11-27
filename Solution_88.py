"""
88. Merge Sorted Array
Easy

2154

224

Add to List

Share
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?

Accepted
1,111,141
Submissions
2,617,507
"""
from typing import List

class Solution:
    def merge_direct(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nu = -1
        mn = 0
        for i in range(-1, -n-1, -1):

            if m==0:
                nums1[:] = nums2[:]

            for j in range(nu-n, -m-n-1, -1):
                print(nums2[i], nums1[j])
                if nums2[i] >= nums1[j]:
                    nums1[j+n-mn]=nums2[i]
                    break
                else:
                    nums1[j+n-mn]=nums1[j]
                    nu-=1
            if nu < -m:
                nums1[0:n+i+1] = nums2[0:n+i+1]

            mn+=1

        return nums1

    def merge_liumang(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:m+n] = nums2

        nums1[:] = sorted(nums1, reverse=False)
        return nums1


if __name__ == '__main__':

    so = Solution()
    print(so.merge([2,0],1,[1],1))

    """
    应该可以复制过去，直接快排；但是我不会快排目前还，所以先用最蠢的方式搞一下试试
    Success Details: 
        Runtime: 63 ms, faster than 8.63% of Python3 online submissions for Merge Sorted Array.
        Memory Usage: 14.3 MB, less than 63.32% of Python3 online submissions for Merge Sorted Array.
        
    MD这种直接搞的都错了好几次，思路一直没捋清楚，两个边界条件都漏了
        · m==0
        · nu先到头儿的。
    ------------------------
    流氓做法：直接内置sorted
    Success Details： 
        Runtime: 40 ms, faster than 45.84% of Python3 online submissions for Merge Sorted Array.
        Memory Usage: 14.4 MB, less than 32.69% of Python3 online submissions for Merge Sorted Array.
    -----------------------
    快排序的后边再尝试吧，另外确实while比for优雅在写题的时候
    
    """