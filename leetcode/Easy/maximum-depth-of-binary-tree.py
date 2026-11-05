// Problem: Maximum Depth of Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// Solved on: 2026-11-05T09:31:13.639Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:


        if root is None:
            return 0

        stack = [(root, 1)]

        best = 0

        while stack:


            node, depth = stack.pop()

            best = max(best, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            
            if node.right:
                stack.append((node.right, depth + 1))
            
          
        
        return best



        