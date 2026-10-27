// Problem: 3Sum Closest
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/3sum-closest/
// Solved on: 2026-10-27T17:48:51.935Z

class Solution:
    '''Keep track of of the absolut diffrence and the sum the hast the least difference is the answer'''
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        best = float('inf')
        closest_sum = 0

      
        for i in range(len(nums) - 2 ):

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                closest = abs(target - total)

                if closest < best:
                    best = min(best, closest) 
                    closest_sum = total

                if total < target:
                    l += 1
                else:
                    r -= 1

        
        return closest_sum

