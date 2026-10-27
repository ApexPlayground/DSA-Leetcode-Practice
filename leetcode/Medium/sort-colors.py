// Problem: Sort Colors
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-colors/
// Solved on: 2026-10-27T17:52:50.172Z

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # sort 0 to front

        pos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
        pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos -= 1
        