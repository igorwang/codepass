# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     1_two_sum
   Description :
   Author :       igorwang
   date：          21/9/2023
-------------------------------------------------
   Change Activity:
                   21/9/2023:
-------------------------------------------------
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            numsMap[nums[i]] = i

        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in numsMap and j != numsMap[complement]:
                return [j, numsMap[complement]]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)
