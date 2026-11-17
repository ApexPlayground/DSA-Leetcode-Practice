// Problem: Permutations
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/permutations/
// Solved on: 2026-11-17T10:22:37.351Z

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        res = []
        path = []

        n = len(nums)

        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if nums[i] in path:
                    continue

                path.append(nums[i])

                backtrack()

                path.pop()
            return
        backtrack()
        return res


        
        