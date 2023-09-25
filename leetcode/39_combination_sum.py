# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     39_combination_sum
   Description :
   Author :       igorwang
   date：          24/9/2023
-------------------------------------------------
   Change Activity:
                   24/9/2023:
-------------------------------------------------
"""

from typing import List


class Solution:
    # def dfs(self, tmp: List, candidates, target, path=[]):
    #     if sum(tmp) > target:
    #         return
    #
    #     if sum(tmp) == target:
    #         path.append(tmp)
    #         return
    #
    #     for i in range(len(candidates)):
    #         new_tmp = sorted(tmp + [candidates[i]])
    #         if sum(new_tmp) > target or new_tmp in path:
    #             continue
    #         self.dfs(new_tmp, candidates, target, path=path)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    solution = Solution()

    candidates = [2, 3, 6, 7]

    target = 7

    result = solution.combinationSum(candidates, target)
    print(result)
