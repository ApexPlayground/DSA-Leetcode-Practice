// Problem: Find Minimum in Rotated Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Solved on: 2026-11-03T07:21:03.685Z

class Solution:
    def findMin(self, nums: list[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]


        