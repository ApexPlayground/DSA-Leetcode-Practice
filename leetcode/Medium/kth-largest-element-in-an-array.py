// Problem: Kth Largest Element in an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
// Solved on: 2026-11-15T11:00:19.428Z

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


        