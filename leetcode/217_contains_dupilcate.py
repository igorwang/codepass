# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     217_contains_dupilcate
   Description :
   Author :       igorwang
   date：          25/9/2023
-------------------------------------------------
   Change Activity:
                   25/9/2023:
-------------------------------------------------
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMaps = {}
        for i in nums:
            if i not in numMaps:
                numMaps[i] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    pass
