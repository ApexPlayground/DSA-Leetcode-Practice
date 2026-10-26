// Problem: Find All Duplicates in an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-all-duplicates-in-an-array/
// Solved on: 2026-10-26T09:20:54.775Z

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            idx = nums[i] - 1
            if nums[i] != nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1
        
        res = []
        for i, v in enumerate(nums):
            if v != (i + 1):
                res.append(v)
        
        return res


        