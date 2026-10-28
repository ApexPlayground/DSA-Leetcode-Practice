// Problem: Permutation in String
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/permutation-in-string/
// Solved on: 2026-10-28T19:03:00.482Z

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        k = len(s1)
        s1_freq = Counter(s1)
        s2_freq = {}

        l = 0

        for r, char in enumerate(s2):

            s2_freq[char] = s2_freq.get(char, 0) + 1

            if (r - l + 1) == k:

                if s1_freq == s2_freq:
                    return True
                
                s2_freq[s2[l]] -= 1

                if  s2_freq[s2[l]] == 0:
                    del  s2_freq[s2[l]]

                l += 1
        
        return False

        