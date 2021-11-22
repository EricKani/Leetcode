"""
14. Longest Common Prefix
Easy

5951

2589

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
Accepted
1,281,773
Submissions
3,358,784
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==1:
            return strs[0]

        lengs = [len(i) for i in strs]

        idx = 0
        for i in range(min(lengs)):
            new_strs = [st[:i+1] for st in strs]
            if len(set(new_strs))==1:
               idx=i+1

        return strs[0][:idx]



if __name__ == '__main__':
    so = Solution()
    print(so.longestCommonPrefix(["a",'ab']))
    """
    1) ["a"]
    2) ["a", "ab"] 开始没有考虑公共string是最短的string整个
    
    Success Details: 
        Runtime: 56 ms, faster than 11.63% of Python3 online submissions for Longest Common Prefix.
        Memory Usage: 14 MB, less than 99.40% of Python3 online submissions for Longest Common Prefix.
    """


