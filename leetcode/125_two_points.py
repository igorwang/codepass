# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     125_two_points
   Description :
   Author :       igorwang
   date：          1/10/2023
-------------------------------------------------
   Change Activity:
                   1/10/2023:
-------------------------------------------------
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = ''.join([c.lower() for c in s if c.isalnum() or c.isalpha()])

        s_reverse = ''.join(reversed(s))
        # for i in range(len(s)):
        #     if s[i] != s_reverse[i]:
        #         return False
        # return True
        return s == s_reverse


if __name__ == '__main__':
    solution = Solution()
    s = "0P"

    result = solution.isPalindrome(s)
    print(result)
