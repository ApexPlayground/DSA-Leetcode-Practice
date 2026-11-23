// Problem: Subarray Sum Equals K
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subarray-sum-equals-k/
// Solved on: 2026-11-23T13:54:53.240Z

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        running_sum = 0
        res = 0

        for i, num in enumerate(nums):
            running_sum += num
            diff = running_sum - k

            if (diff) in seen:
                res += seen[diff]
            
            seen[running_sum] = seen.get(running_sum, 0) + 1
        
        return res
            


        