// Problem: Lowest Common Ancestor of a Binary Search Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
// Solved on: 2026-11-25T18:44:33.995Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):

            if not node:
                return None
            
            if node.val > p.val and node.val > q.val:
                return dfs(node.left)
            
            elif node.val < p.val and node.val < q.val:
                return dfs(node.right)
            else:
                return node
        
        return dfs(root)