// Problem: Insert into a Binary Search Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/insert-into-a-binary-search-tree/
// Solved on: 2026-11-25T23:03:11.853Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:



        def dfs(node):
            if not node:
                return TreeNode(val)

            
            if node.val > val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            
            return node
        
       

        return  dfs(root)
        