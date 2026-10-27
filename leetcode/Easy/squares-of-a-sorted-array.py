// Problem: Squares of a Sorted Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/squares-of-a-sorted-array/
// Solved on: 2026-10-27T08:45:00.206Z

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1

        res = [0] * len(nums)
        idx = r

        while l < r:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = abs(nums[l])**2
                idx -= 1
                l += 1
            else:
                res[idx] = abs(nums[r])**2
                idx -= 1
                r -= 1
        
        # last value
        res[0] =  abs(nums[l])**2

        return res





        