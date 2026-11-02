// Problem: Find Peak Element
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-peak-element/
// Solved on: 2026-11-02T20:08:51.536Z

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif nums[mid] > nums[mid + 1]:
                r = mid
        return l
        