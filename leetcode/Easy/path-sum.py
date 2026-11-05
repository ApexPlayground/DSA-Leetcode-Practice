// Problem: Path Sum
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/path-sum/
// Solved on: 2026-11-05T12:53:23.416Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def dfs(node, target):

            if not node:
                return False

            target -= node.val

            if not node.left and not node.right:
                return target == 0

            left = dfs(node.left, target)
            right = dfs(node.right, target)

            return left or right
        
        return dfs(root, targetSum)
            




        