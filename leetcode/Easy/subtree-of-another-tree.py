// Problem: Subtree of Another Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subtree-of-another-tree/
// Solved on: 2026-11-08T12:42:59.786Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def isSame(node1, node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            left = isSame(node1.left, node2.left)
            right = isSame(node1.right, node2.right)

            return left and right
        
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val and isSame(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
            


        