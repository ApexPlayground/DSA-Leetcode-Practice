// Problem: Product of Array Except Self
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/product-of-array-except-self/
// Solved on: 2026-10-26T09:07:06.748Z

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        res = []

        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         ans *= nums[j]
        #     res.append(ans)
        # return res
            

        p_prod = [1] * len(nums)
        s_prod = [1] * len(nums)

        # prefix prod
        for i in range(1, len(nums)):
            p_prod[i] = p_prod[i - 1] * nums[i - 1] 
        
        print(p_prod)

        #suffix prod
        for i in range(len(nums) - 2, -1, -1):
            s_prod[i] = s_prod[i + 1] * nums[i + 1] 
        
        print(s_prod)

        ans = []
        for v1, v2 in zip(p_prod, s_prod):
            ans.append(v1 * v2)
        
        return ans

        