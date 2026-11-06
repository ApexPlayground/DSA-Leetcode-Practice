// Problem: Subtree of Another Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subtree-of-another-tree/
// Solved on: 2026-11-06T08:23:07.508Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def dfs(node, subNode):

            if not node and not subNode:
                return True
            
            if not node or not subNode:
                return False

            if node.val == subNode.val and isSame(node, subNode):
                return True

            left = dfs(node.left, subNode)
            right = dfs(node.right, subNode)

            return left or right
        
        def isSame(nodeOne, nodeTwo):

            if not nodeOne and not nodeTwo:
                return True
            
            if not nodeOne or not nodeTwo:
                return False
            
            if nodeOne.val != nodeTwo.val:
                return False
            
            left = isSame(nodeOne.left, nodeTwo.left)
            right = isSame(nodeOne.right, nodeTwo.right)

            return left and right
        
        return dfs(root, subRoot)

        