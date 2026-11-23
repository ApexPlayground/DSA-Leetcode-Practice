// Problem: Group Anagrams
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/group-anagrams/
// Solved on: 2026-11-23T10:06:20.470Z

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = defaultdict(list)

        for word in strs:
            freq = Counter(word)
            keyword = frozenset(freq.items())

            res[keyword].append(word)
        
        return list(res.values())

        