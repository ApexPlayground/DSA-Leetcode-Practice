// Problem: Top K Frequent Elements
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/top-k-frequent-elements/
// Solved on: 2026-11-23T10:18:13.632Z

import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        heap = []

        freq_arr = [(val, key) for key, val in Counter(nums).items()]

        for item in freq_arr:
            heapq.heappush(heap, item)

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [num for _, num in heap]

        return res


        