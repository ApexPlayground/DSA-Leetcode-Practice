// Problem: Binary Tree Maximum Path Sum
// Platform: leetcode
// Rating/Difficulty: Hard
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
// Solved on: 2026-11-26T13:55:04.980Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        best = float('-inf')
        def dfs(node):
            nonlocal best

            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            best = max(best, (left + node.val + right))

            return node.val + max(left, right)
        
        dfs(root)
        return best





        