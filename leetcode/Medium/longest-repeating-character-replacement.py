// Problem: Longest Repeating Character Replacement
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-repeating-character-replacement/
// Solved on: 2026-10-28T18:51:31.951Z

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """ For this question i used a hashmap because it helps
        finding the max frequency in the current window, 
        and when we subtract it from the window length we
        can check if we have exceeded k limit, then shink acordingly """

        freq = {}
        l = 0
        best = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            longest = max(freq.values())


            while (r - l + 1) - longest > k:
                freq[s[l]] -= 1

                l += 1
            

            best = max(best, r - l + 1)

        return best


        