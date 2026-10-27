// Problem: Backspace String Compare
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/backspace-string-compare/
// Solved on: 2026-10-27T16:46:23.716Z

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        i = len(s) - 1
        j = len(t) - 1


        while i >= 0 or j >= 0:

            skip_s = 0
            skip_t = 0

            # valid char for s
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                elif skip_s > 0:
                    skip_s -= 1
                else:
                    break
                
                i -= 1
            # valid char for t
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                elif skip_t > 0:
                    skip_t -= 1
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
            



                


     



        
       
        # s_stack = []

        # for char in s:
        #     if char == '#':
        #         if s_stack:
        #             s_stack.pop()
        #         continue
        #     s_stack.append(char)
        
        # t_stack = []

        # for char in t:
        #     if char == '#':
        #         if t_stack:
        #                 t_stack.pop()
        #         continue
        #     t_stack.append(char)
        
        # print(s_stack)
        # print(t_stack)
        # return s_stack == t_stack

        