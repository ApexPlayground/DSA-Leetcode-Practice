// Problem: Binary Tree Paths
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-paths/
// Solved on: 2026-11-08T13:05:27.110Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        res = []
        

        def dfs(node, path):
            if not node:
                return 
            
            path += str(node.val)
            
            if not node.left and not node.right:
                res.append(path)
           
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")
        
        dfs(root, "")

        return res

        