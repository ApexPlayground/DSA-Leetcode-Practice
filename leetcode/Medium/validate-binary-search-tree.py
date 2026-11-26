// Problem: Validate Binary Search Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/validate-binary-search-tree/
// Solved on: 2026-11-26T11:57:45.313Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(node, min_val, max_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False
            
            left = dfs(node.left, min_val, node.val)
            right = dfs(node.right, node.val, max_val)

            return left and right
        
        return dfs(root, float('-inf'), float('inf'))


        