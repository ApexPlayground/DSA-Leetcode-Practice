// Problem: Kth Smallest Element in a BST
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
// Solved on: 2026-11-24T10:14:04.356Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        ans = 0
        kth = k
        def dfs(node):
            nonlocal ans, kth

            if not node:
                return
            
            dfs(node.left)

            kth -= 1
            if kth == 0:
                ans = node.val
                return 

            dfs(node.right)

        dfs(root)
        return ans            
        