// Problem: Backspace String Compare
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/backspace-string-compare/
// Solved on: 2026-10-27T09:07:48.597Z

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
       
        s_stack = []

        for char in s:
            if char == '#':
                if s_stack:
                    s_stack.pop()
                continue
            s_stack.append(char)
        
        t_stack = []

        for char in t:
            if char == '#':
                if t_stack:
                        t_stack.pop()
                continue
            t_stack.append(char)
        
        print(s_stack)
        print(t_stack)
        return s_stack == t_stack

        