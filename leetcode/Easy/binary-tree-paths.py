// Problem: Binary Tree Paths
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-paths/
// Solved on: 2026-11-06T08:41:07.526Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        path_str = ""
        res = []

        def dfs(node, path_str):
            if not node:
                return
            
            path_str += str(node.val)

            if not node.left and not node.right:
                res.append("".join(path_str))
                return


            dfs(node.left, path_str + "->")
            dfs(node.right, path_str + "->")
        
        dfs(root, path_str)
        return res

            

        