from typing import List
import time

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





if __name__ == '__main__':
    me = Solution_45()
    print(me.jump([1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))