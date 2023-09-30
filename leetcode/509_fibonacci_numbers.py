# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     509_ fibonacci_numbers
   Description :
   Author :       igorwang
   date：          30/9/2023
-------------------------------------------------
   Change Activity:
                   30/9/2023:
-------------------------------------------------
"""


class Solution:
    def fib(self, n: int, mems={}) -> int:
        if n in mems:
            return mems[n]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        mems[n] = self.fib(n - 1, mems) + self.fib(n - 2, mems)
        return mems[n]

if __name__ == '__main__':
    pass