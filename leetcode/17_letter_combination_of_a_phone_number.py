# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17_letter_combination_of_a_phone_number
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
    def dfs(self, tmp, index, letters, path=[]):
        if len(tmp) == len(letters):
            path.append(tmp)
            return
        for char in letters[index]:
            self.dfs(tmp + char, index + 1, letters, path)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0 or len(digits) > 4:
            return []

        number2letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mon",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        letters = [number2letter[i] for i in list(digits)]
        path = []
        self.dfs("", 0, letters, path)
        return path


if __name__ == '__main__':
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(result)
