# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     49_group_anagrams
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            char_hashmap = [0] * 26
            for c in string:
                char_hashmap[ord(c) - ord('a')] += 1
            # key = "".join([chr(j + ord('a')) + str(i) for j, i in enumerate(char_hashmap) if i != 0])
            key = tuple(char_hashmap)
            if key not in res:
                res[key] = [string]
            else:
                res[key].append(string)
        return list(res.values())


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = solution.groupAnagrams(strs)
    print(result)
