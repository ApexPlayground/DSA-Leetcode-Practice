// Problem: Kth Largest Element in an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
// Solved on: 2026-11-15T10:50:39.360Z

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        max_heap = [-x for x in nums]

        heapq.heapify(max_heap)

        for _ in range(k - 1):
            heapq.heappop(max_heap)
        
        ans = -heapq.heappop(max_heap)

        return ans


        