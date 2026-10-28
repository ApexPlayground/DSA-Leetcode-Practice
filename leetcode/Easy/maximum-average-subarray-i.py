// Problem: Maximum Average Subarray I
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/maximum-average-subarray-i/
// Solved on: 2026-10-28T12:30:19.582Z

class Solution:
    """ Using a fixed sliding window, when i get to lenght k, i do the calculation, save the result and update the window"""
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        l = 0
        total = 0
        best = float('-inf')

        for r in range(len(nums)):
            total += nums[r]

            if (r - l) + 1 == k:
               
                best = max(best, total)

                # update window
                total -= nums[l]
                l += 1
        
        return best / k

        