// Problem: Product of Array Except Self
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/product-of-array-except-self/
// Solved on: 2026-10-26T09:17:40.500Z

class Solution:
    '''the idea is to use a prefix and suffix product array, build up both array,
    when we ar multiplying prefix * suffix at i, it dosnt include i so that is the product
    of all values except i.'''
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # prefix product
        prefix_prod = [1] * n

        # suffix product
        suffix_prod = [1] * n

        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix_prod[i] = suffix_prod[i + 1] * nums[i + 1]
        
        res = []
        for val1, val2 in zip(prefix_prod, suffix_prod):
            res.append(val1 * val2)
        
      
        return res

         
        