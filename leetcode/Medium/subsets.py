// Problem: Subsets
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subsets/
// Solved on: 2026-11-16T20:52:39.693Z

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        path = []
        res = []

        def backtrack(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i + 1)

                path.pop()
            
            return
        
        backtrack(0)
        return res


        