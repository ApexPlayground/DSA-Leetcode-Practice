// Problem: Squares of a Sorted Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/squares-of-a-sorted-array/
// Solved on: 2026-10-27T08:44:07.794Z

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [(num ** 2) for num in nums]
        res = [0] * len(nums)

        l, r = 0, len(nums) - 1
        pos = r

        while l <= r:
            if nums[l] >= nums[r]:
               res[pos] = nums[l]
               pos -= 1
               l += 1
               
            else:
                res[pos] = nums[r]
                pos -= 1
                r -= 1
                
        return res

        