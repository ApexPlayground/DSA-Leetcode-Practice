// Problem: Invert Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/invert-binary-tree/
// Solved on: 2026-11-05T12:18:54.235Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            node.left = right
            node.right = left

            return node



          
        
        return dfs(root)

        