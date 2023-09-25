# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     242_valid_anagram
   Description :
   Author :       igorwang
   date：          26/9/2023
-------------------------------------------------
   Change Activity:
                   26/9/2023:
-------------------------------------------------
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for i in s:
            if i not in sMap:
                sMap[i] = 1
            else:
                sMap[i] += 1

        for i in t:
            if i not in tMap:
                tMap[i] = 1
            else:
                tMap[i] += 1
        return sMap == tMap


if __name__ == '__main__':
    pass
