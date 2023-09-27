# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     128_longest_consecutive_sequence
   Description :
   Author :       igorwang
   date：          27/9/2023
-------------------------------------------------
   Change Activity:
                   27/9/2023:
-------------------------------------------------
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_sets = set(nums)
        maxLen = 0
        # start_nums = []
        for i in nums_sets:
            if (i - 1) not in nums_sets:
                length = 1
                while (i + length) in nums_sets:
                    length += 1
                maxLen = max(length, maxLen)
        return maxLen


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 3, 993, 23423432]
    result = solution.longestConsecutive(nums=nums)
    print(result)
