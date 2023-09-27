# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     347_top_k_frequent_elements
   Description :
   Author :       igorwang
   date：          26/9/2023
-------------------------------------------------
   Change Activity:
                   26/9/2023:
-------------------------------------------------
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        for i in nums:
            if i not in numsMap:
                numsMap[i] = 1
            else:
                numsMap[i] += 1

        maxHeap = [[] for i in range(max(numsMap.values()) + 1)]
        for num, count in numsMap.items():
            maxHeap[count].append(num)

        result = []
        for j in range(len(maxHeap) - 1, -1, -1):
            if not maxHeap[j]:
                continue
            result.extend(maxHeap[j][:k - len(result)])
            if len(result) == k:
                return result
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 0, 1, 0]

    k = 1
    result = solution.topKFrequent(nums, k)
    print(result)
