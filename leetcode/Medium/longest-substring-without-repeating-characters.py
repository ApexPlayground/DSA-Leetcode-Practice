// Problem: Longest Substring Without Repeating Characters
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Solved on: 2026-10-28T12:54:23.143Z

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        best = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            best = max(best, len(seen))
        
        return best
        

        