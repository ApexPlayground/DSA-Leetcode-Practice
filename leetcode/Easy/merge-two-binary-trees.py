// Problem: Merge Two Binary Trees
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-two-binary-trees/
// Solved on: 2026-11-08T15:23:49.008Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:

        def dfs(node1, node2):

            if not node1 and not node2:
                return None
            
            if node1 and node2:
                merged = TreeNode(node1.val + node2.val)


            if not node1:
                return node2
            if not node2:
                return node1
            
            merged.left = dfs(node1.left, node2.left)
            merged.right = dfs(node1.right, node2.right)
        
            return merged
        
        return dfs(root1, root2)

        