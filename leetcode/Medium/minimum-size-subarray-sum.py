// Problem: Minimum Size Subarray Sum
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/minimum-size-subarray-sum/
// Solved on: 2026-10-28T13:19:52.811Z

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        l = 0
        total = 0

        best = float('inf')
      

        for r in range(len(nums)):

            total += nums[r]
           

            while total >= target:
                best = min(best, r - l + 1)

                total -= nums[l]
                l += 1
                
        return best if best < float('inf') else 0
        
     

       



        
        