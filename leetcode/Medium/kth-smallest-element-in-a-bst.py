// Problem: Kth Smallest Element in a BST
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
// Solved on: 2026-11-16T15:48:47.007Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        heap = []

        def dfs(node):
            if not node:
                return 
            
            heappush(heap, -node.val)

            if len(heap) > k:
                heapq.heappop(heap)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return -heap[0]
        