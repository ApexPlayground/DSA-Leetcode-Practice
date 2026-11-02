// Problem: Binary Search
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-search/
// Solved on: 2026-11-02T19:24:02.903Z

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


        