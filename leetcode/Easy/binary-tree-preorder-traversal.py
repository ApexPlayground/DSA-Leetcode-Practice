// Problem: Binary Tree Preorder Traversal
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-preorder-traversal/
// Solved on: 2026-11-25T16:46:54.917Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):

            if not node:
                return

            res.append(node.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res
            
        




        