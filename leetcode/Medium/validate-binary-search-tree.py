// Problem: Validate Binary Search Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/validate-binary-search-tree/
// Solved on: 2026-11-24T09:52:29.322Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(node, _min, _max):

            if not node:
                return True

            if not (_min < node.val < _max):
                return False
            
            left = dfs( node.left, _min, node.val)
            right = dfs( node.right, node.val, _max)

            return left and right
        
        return dfs(root, float('-inf'), float('inf'))





