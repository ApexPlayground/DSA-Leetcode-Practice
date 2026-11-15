// Problem: K Closest Points to Origin
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/k-closest-points-to-origin/
// Solved on: 2026-11-15T12:55:28.424Z

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = []

        for x, y in points:
            dis = (0 - x)**2 + (0 - y)**2
            
            heapq.heappush(heap, (-dis, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [cord for dis, cord in heap]

        return res





        