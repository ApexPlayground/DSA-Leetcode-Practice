// Problem: Subtree of Another Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subtree-of-another-tree/
// Solved on: 2026-11-25T18:02:53.809Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, node1, node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            
            left = self.isSame(node1.left, node2.left)
            right = self.isSame(node1.right, node2.right)

            return left and right

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def dfs(node):
            if not node:
                return False
            
            if self.isSame(node, subRoot):
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right
        
        return dfs(root)
    
   