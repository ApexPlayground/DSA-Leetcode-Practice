// Problem: Binary Tree Paths
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-paths/
// Solved on: 2026-11-06T08:35:48.674Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(node, valid):
            if not node:
                return
            # add node value to valid list
            valid.append(str(node.val))

            # if no child we have gotten to end of the path
            if not node.left and not node.right:
                res.append("->".join(valid))
            else: # if there are children
                backtrack(node.left, valid)
                backtrack(node.right, valid)
            
            valid.pop()
        backtrack(root, [])
        return res





        