// Problem: Majority Element
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/majority-element/
// Solved on: 2026-10-26T08:19:05.670Z

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        choice = 0
        count = 0

        for num in nums:
            if count == 0:
                choice = num
                count = 1
            elif num == choice:
                count += 1
            else:
                count -= 1
        return choice
        


        