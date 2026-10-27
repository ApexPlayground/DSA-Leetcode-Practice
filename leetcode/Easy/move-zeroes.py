// Problem: Move Zeroes
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/move-zeroes/
// Solved on: 2026-10-27T08:22:57.218Z

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] =  nums[index], nums[i]
                index += 1
        