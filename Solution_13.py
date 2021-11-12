"""
13. Roman to Integer
Easy

2215

164

Add to List

Share
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
Accepted
1,225,027
Submissions
2,124,424
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        di = dict()
        di['I'] = 1
        di['V'] = 5
        di['X'] = 10
        di['L'] = 50
        di['C'] = 100
        di['D'] = 500
        di['M'] = 1000


        if len(s)==1:
            return di[s]
        else:
            res = 0
            mark = False
            for i in range(len(s)-1):
                if mark:
                    mark=False
                    continue
                if di[s[i]]>=di[s[i+1]]:
                   res+=di[s[i]]
                else:
                    res+=di[s[i+1]]-di[s[i]]
                    mark=True
            if di[s[-1]]<=di[s[-2]]:
                res+=di[s[-1]]
            return res




if __name__ == '__main__':
    so = Solution()
    print(so.romanToInt('IV'))
    """
    Success Details: 
        Runtime: 48 ms, faster than 72.40% of Python3 online submissions for Roman to Integer.
        Memory Usage: 14.2 MB, less than 84.12% of Python3 online submissions for Roman to Integer.
    题目不难，细节漏了很多：
        1）最开始题没读清楚，以位就那几个单独的数字是特例；后来发现是要用来组合新数字的
        2）确实没考虑到len(s)==1的情况
        3）<= 还是<之类的问题也写的时候check一下
    """