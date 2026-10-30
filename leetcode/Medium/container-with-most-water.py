// Problem: Container With Most Water
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/container-with-most-water/
// Solved on: 2026-10-30T04:39:18.206Z

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1

        best = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            best = max(best, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return best

        