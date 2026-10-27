// Problem: 3Sum Closest
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/3sum-closest/
// Solved on: 2026-10-27T17:41:27.837Z

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
 

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                curr = nums[i] + nums[j] + nums[k]

                if abs(curr - target) <= abs(res - target):
                    res = curr

                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    return curr
        return res

        