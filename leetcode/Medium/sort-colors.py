// Problem: Sort Colors
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-colors/
// Solved on: 2026-10-27T18:15:18.257Z

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """ Basically the ideas is to use 3 pointers, when we swap l with pos,
        we are confident that we dont have to go back anymore for we increment pos and l,
        when we swap with r, we dont know what we swapped with do we do not update pos forward"""
        pos = 0

        l = 0
        r = len(nums) - 1

        while pos <= r:

            if nums[pos] == 0:
                nums[pos], nums[l] = nums[l], nums[pos]
                l += 1
                pos += 1
            elif nums[pos] == 1:
                pos += 1
            else:
                nums[pos], nums[r] = nums[r], nums[pos]
                r -= 1
            
           
            
            
            



        # """ sort 0's to the front and 2's ro the back"""

        # # sort 0 to front

        # pos = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[pos], nums[i] = nums[i], nums[pos]
        #         pos += 1
        
        # pos = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == 2:
        #         nums[pos], nums[i] = nums[i], nums[pos]
        #         pos -= 1
        