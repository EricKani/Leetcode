from typing import List
import time


# 221 最大正方形
class Solution_221:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare


    def maximalSquare_dynamic(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare








# 1344 时钟指针的夹角
class Solution_clockangle:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_h = hour%12*30+minutes/60*30
        angle_m = minutes/60 * 360
        a1 = abs(angle_h-angle_m)
        a2 = 360-a1
        return min(a1,a2)

class Solution_45:
    def jump(self, nums: List[int]) -> int:
        ### 这种思路时间复杂度过高，会超过c++和python的时间限制
        if len(nums)<=1:
            return 0

        nums = nums[::-1]
        times = 0
        idx = 0
        while idx < len(nums)-1:
            maybe = []
            nums = nums[idx:]
            for i in range(1, len(nums)):
                if nums[i]>=i:
                    maybe.append(i)
            print(maybe)
            maybe = sorted(maybe, reverse=True)
            idx = maybe[0]
            times+=1
        return times
    def jump(self, nums:List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

def main():
    so = Solution_221()
    print(so.maximalSquare([['1', '0', '1', '0', '1', '0'] * 10000, ['1', '0', '1', '1', '1', '0'] * 10000,
                            ['1', '0', '1', '1', '1', '0'] * 10000, ['1', '0', '1', '1', '1', '0'] * 10000,
                            ['1', '0', '1', '0', '1', '0'] * 10000] * 1000))




if __name__ == '__main__':
    # main()
    me = Solution_45()
    print(me.jump([1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))