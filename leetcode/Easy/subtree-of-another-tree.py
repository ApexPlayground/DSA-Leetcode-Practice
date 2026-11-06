// Problem: Subtree of Another Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subtree-of-another-tree/
// Solved on: 2026-11-06T08:15:48.901Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if self.same_tree(root, subRoot):
            return True
        
    
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
        

    def same_tree(self, t1, t2):

        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False
        
        if t1 and t2:
            if t1.val == t2.val:
                left = self.same_tree(t1.left, t2.left)
                right = self.same_tree(t1.right, t2.right)
                return left and right
            else:
                return False



        

        