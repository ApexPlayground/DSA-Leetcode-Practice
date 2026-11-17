// Problem: Permutations
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/permutations/
// Solved on: 2026-11-17T10:20:05.233Z

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        seen = set()
        def helper(path):

            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if nums[i] in seen:
                    continue
                
                seen.add(nums[i])
                path.append(nums[i])

                helper(path)

                val = path.pop()
                seen.remove(val)

            


        helper([])
        return res
        