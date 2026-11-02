// Problem: Find Peak Element
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-peak-element/
// Solved on: 2026-11-02T19:48:51.915Z

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # k = max(nums)
        # l = 0
        # r = len(nums) - 1

        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] == k:
        #         return mid
        #     elif nums[mid] > nums[l]:
        #         r = mid
        #     else:
        #         l = mid + 1
        # return -1
       
        if len(nums) == 1:
            return 0

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
                
        
        # check the first and last
        n = len(nums)
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
