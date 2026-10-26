// Problem: Find All Duplicates in an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-all-duplicates-in-an-array/
// Solved on: 2026-10-26T11:15:00.946Z

class Solution:

    '''This is quite smart, when we see a number for the first time,
    we use the number minus one to find an index and mark the value at that index as negative.
    If we see the same number again, we'll check that same index,
    and if it's already negative value, we know it's a duplicate. '''

    def findDuplicates(self, nums: list[int]) -> list[int]:

        n = len(nums)
        res = []

        for i in range(n):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                res.append(abs(nums[i]))
            else:
                nums[index] *= -1
        
        return res


        