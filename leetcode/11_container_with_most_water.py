# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11_container_with_most_water
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
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    print(result)
