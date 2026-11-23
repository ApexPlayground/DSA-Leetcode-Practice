// Problem: Contiguous Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/contiguous-array/
// Solved on: 2026-11-23T15:24:56.130Z

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        prefix = {0: -1}
        best = 0

        running_sum = 0

        for i, num in enumerate(nums):
            if num == 0:
                running_sum -= 1
            else:
                running_sum += 1
            
            if running_sum in prefix:
                best = max(best, i - prefix[running_sum])
            else:
                prefix[running_sum] = i
        
        return best



        