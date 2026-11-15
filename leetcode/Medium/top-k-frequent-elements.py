// Problem: Top K Frequent Elements
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/top-k-frequent-elements/
// Solved on: 2026-11-15T11:10:21.221Z

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        heap = []

        for key, val in freq.items():
            heap.append((val, key))
        
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        print(heap)
        
        ans = [num for count, num in heap]

        print(ans)

        return ans
        


        