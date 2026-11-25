// Problem: Balanced Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/balanced-binary-tree/
// Solved on: 2026-11-25T17:33:17.311Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        balanced = True
        def dfs(node):
            nonlocal balanced 

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                balanced = False
            
            return  1 + max(left, right)
        
        dfs(root)
        return balanced


        