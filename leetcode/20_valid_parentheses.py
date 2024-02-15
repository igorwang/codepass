# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20_valid_parentheses
   Description :
   Author :       igorwang
   date：          15/2/2024
-------------------------------------------------
   Change Activity:
                   15/2/2024:
-------------------------------------------------
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # my solution
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top_element = stack[-1]
                if (top_element == '(' and i == ')') \
                        or (top_element == '{' and i == '}') \
                        or (top_element == '[' and i == ']'):
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == '__main__':
    solution = Solution()
    s = "()({[]})(())()"
    result = solution.isValid(s)
    print(result)
