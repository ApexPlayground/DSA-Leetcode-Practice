// Problem: Is Subsequence
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/is-subsequence/
// Solved on: 2026-10-28T12:49:10.586Z

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

       

        l = 0
        for r in range(len(t)):
            if l == len(s):
                return True

            if t[r] == s[l]:
                l += 1
        
        print(l)
        return l == len(s)

        