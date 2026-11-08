// Problem: Invert Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/invert-binary-tree/
// Solved on: 2026-11-08T12:14:54.041Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return root
        
        def dfs(node):

            if not node:
                return

            if not node.left and not node.right:
                return 
            
            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return root
        