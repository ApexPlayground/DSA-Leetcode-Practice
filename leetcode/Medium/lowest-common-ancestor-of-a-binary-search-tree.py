// Problem: Lowest Common Ancestor of a Binary Search Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
// Solved on: 2026-11-16T15:26:36.328Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        queue = collections.deque([])

        curr = root

        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr

        