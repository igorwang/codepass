# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     238_product_of_array_except_self
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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = postfix * output[i]
            postfix = postfix * nums[i]

        return output


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 1, 0, -3, 3]

    result = solution.productExceptSelf(nums)
    print(result)
