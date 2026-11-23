// Problem: Group Anagrams
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/group-anagrams/
// Solved on: 2026-11-23T09:59:19.949Z

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for val in strs:
            sorted_str = sorted(val)
            key_str = "".join(sorted_str)
            group[key_str].append(val)
        
        return list(group.values())
        