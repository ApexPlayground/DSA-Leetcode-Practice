// Problem: Kth Smallest Element in a BST
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
// Solved on: 2026-11-24T10:27:48.677Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        ans = 0

        def dfs(node):
            nonlocal ans, k

            if not node:
                return 
            
            dfs(node.left)

            k -= 1

            if k == 0:
                ans = node.val
            
            dfs(node.right)
        
        dfs(root)
        return ans

            


        