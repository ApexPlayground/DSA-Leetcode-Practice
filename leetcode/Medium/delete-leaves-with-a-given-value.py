// Problem: Delete Leaves With a Given Value
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/delete-leaves-with-a-given-value/
// Solved on: 2026-11-26T12:31:04.593Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:

        def dfs(node):

            if not node:
                return None

            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.left and not node.right:
                if node.val == target:
                    return None

            return node
        
        return dfs(root)

        