// Problem: Subarray Product Less Than K
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subarray-product-less-than-k/
// Solved on: 2026-10-28T20:31:55.893Z

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        # prod = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     prod[i] = prod[i - 1] * nums[i - 1]

        # print(prod)

        # total

        """
        Omo, this was kind of hard. The idea is to maintain a valid window
        and count the valid range rather than individual subarrays.
        """

        if k <= 1:
            return 0

        total = 1
        count = 0

        l = 0

        for r, num in enumerate(nums):
            total *= num

            while total >= k:
                total //= nums[l]

                l += 1

            count += r - l + 1

        return count
