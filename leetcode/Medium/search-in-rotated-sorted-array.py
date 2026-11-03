// Problem: Search in Rotated Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
// Solved on: 2026-11-03T06:58:46.460Z

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                # go left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            elif nums[m] <= nums[r]:
                if nums[m]  < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


        