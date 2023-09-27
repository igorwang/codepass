# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     36_valid_sudoku
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
    # my solution
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [[0] * 9 for i in range(9)]
        columns = [[0] * 9 for i in range(9)]
        boxes = [[0] * 9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                boxe_index = i // 3 + (j // 3) * 3
                num = board[i][j]
                if num == '.':
                    continue
                num = int(num) - 1
                if rows[i][num] == 1 or columns[j][num] == 1 or boxes[boxe_index][num] == 1:
                    return False
                rows[i][num] = 1
                columns[j][num] = 1
                boxes[boxe_index][num] = 1
        return True


if __name__ == '__main__':
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = solution.isValidSudoku(board=board)
    print(result)
