// Problem: Kth Smallest Element in a Sorted Matrix
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
// Solved on: 2026-11-15T13:50:02.765Z

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq

        arr = [item for row in matrix for item in row]
        
        heapq.heapify(arr)

        for _ in range(k - 1):
            heapq.heappop(arr)
        
        return arr[0]

        