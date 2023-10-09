# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     42_trapping_rain_water
   Description :
   Author :       igorwang
   date：          9/10/2023
-------------------------------------------------
   Change Activity:
                   9/10/2023:
-------------------------------------------------
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


if __name__ == '__main__':
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(height)
    print(result)
