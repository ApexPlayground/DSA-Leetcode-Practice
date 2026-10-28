// Problem: Backspace String Compare
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/backspace-string-compare/
// Solved on: 2026-10-28T12:13:42.203Z

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:

            s_skip = 0
            t_skip = 0

            while i >= 0:
                if s[i] == "#":
                    s_skip += 1
                elif s_skip > 0:
                    s_skip -= 1
                else:
                    break
                
                i -= 1
            
            while j >= 0:
                if t[j] == "#":
                    t_skip += 1
                elif t_skip > 0:
                    t_skip -= 1
                else:
                    break
                
                j -= 1
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False   
            elif i >= 0 or j >= 0:
                return False
            
            i -= 1
            j -= 1
        return True

            
        