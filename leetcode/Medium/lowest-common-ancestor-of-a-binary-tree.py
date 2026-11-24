// Problem: Lowest Common Ancestor of a Binary Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// Solved on: 2026-11-24T10:12:26.734Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
for this question the moment we find a node that is p or q, we return it immediately
and check the right if we find bothe return the parent node if not return only the node we find 
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):

            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            return left or right
        
        return dfs(root)
            

        