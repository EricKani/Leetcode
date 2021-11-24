"""
17. Letter Combinations of a Phone Number
Medium

7977

598

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
Accepted
1,008,500
Submissions
1,934,408
"""
from typing import List

class Solution:
    def merge(self, li1, li2):
        res = []
        for i in li1:
            for j in li2:
                res.append(i+j)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits)==0:
            return res


        di = dict()
        di['2'] = ['a','b','c']
        di['3'] = ['d','e','f']
        di['4'] = ['g','h','i']
        di['5'] = ['j','k','l']
        di['6'] = ['m','n','o']
        di['7'] = ['p','q','r','s']
        di['8'] = ['t','u','v']
        di['9'] = ['w','x','y','z']

        if len(digits)==1:
            return di[digits]

        res = di[digits[0]]
        for i in range(1, len(digits)):
            res = self.merge(res, di[digits[i]])
        return res

if __name__ == '__main__':
    So = Solution()
    print(So.letterCombinations('23'))

    """
    Success Details: 
        Runtime: 48 ms, faster than 12.21% of Python3 online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 14.4 MB, less than 34.25% of Python3 online submissions for Letter Combinations of a Phone Number.
    
    # 效率不是很高，只是实现了
    """