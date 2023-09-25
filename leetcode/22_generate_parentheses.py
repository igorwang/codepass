# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     22_generate_parentheses
   Description :
   Author :       igorwang
   date：          22/9/2023
-------------------------------------------------
   Change Activity:
                   22/9/2023:
-------------------------------------------------
"""

from typing import List


class Solution:
    def dfs(self, tmp, n, cnt_o, cnt_c, path=[]):
        if len(tmp) == 2 * n:
            path.append(tmp)
            return

        if cnt_o < n:
            self.dfs(tmp + '(', n, cnt_o + 1, cnt_c, path=path)

        if cnt_c < cnt_o:
            self.dfs(tmp + ')', n, cnt_o, cnt_c + 1, path=path)

    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0 or n > 8:
            return []

        path = []
        self.dfs("", n, 0, 0, path)
        return path


if __name__ == '__main__':
    solution = Solution()
    n = 4
    result = solution.generateParenthesis(n)
    print(result)
