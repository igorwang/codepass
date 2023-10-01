# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     2_two_sum_ii_input_array_is_sorted
   Description :
   Author :       igorwang
   date：          1/10/2023
-------------------------------------------------
   Change Activity:
                   1/10/2023:
-------------------------------------------------
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numMap = {}
        for i in range(len(numbers)):
            numMap[numbers[i]] = i + 1

        for j in range(len(numbers)):
            completed = target - numbers[j]
            if completed in numMap and (j + 1) != numMap[completed]:
                if j + 1 < numMap[completed]:
                    return [j + 1, numMap[completed]]
                else:
                    return [numMap[completed], j + 1]
        return []


if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9

    result = solution.twoSum(numbers, target)
    print(result)
