"""
36. Valid Sudoku
Medium

3891

644

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
Accepted
610,313
Submissions
1,138,591
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        arr = np.array(board)
        print(arr)
        for i in range(arr.shape[0]):
            if len(set(arr[i])) - (arr[i]!='.').sum()<1:
                return False
        for j in range(arr.shape[1]):
            if len(set(arr[:,j])) - (arr[:,j]!='.').sum()<1:
                print(11)
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                if len(set(list(arr[i:i+3, j:j+3].reshape(-1)))) - (arr[i:i+3, j:j+3] != '.').sum() < 1:
                    return False
        return True
if __name__ == '__main__':
    so = Solution()
    print(so.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]))

    """
    Success Details:  
        Runtime: 280 ms, faster than 5.08% of Python3 online submissions for Valid Sudoku.
        Memory Usage: 30.8 MB, less than 15.89% of Python3 online submissions for Valid Sudoku.
        
    
    思路是对的，用set来去重：虽然解决了，但是太取巧了，用了外来包numpy，而且效率也不高，主要是取square不是很熟悉，可以参考下边的python用法：
        这种写法用的不多。
        In [8]: [x+y for x in range(0,  3) for y in range(0, 3)]
        Out[8]: [0, 1, 2, 1, 2, 3, 2, 3, 4]
        
        取列就用zip（*board就可以了）
    
    纯python实现反而快了些，估计是numpy的效果在这么小的矩阵下无法凸显2333
    Success Details:
        Runtime: 141 ms, faster than 18.74% of Python3 online submissions for Valid Sudoku.
        Memory Usage: 14.4 MB, less than 43.88% of Python3 online submissions for Valid Sudoku.
    
    """