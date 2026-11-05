// Problem: Invert Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/invert-binary-tree/
// Solved on: 2026-11-05T12:36:04.213Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return None
        
        queue = collections.deque([root])

        while queue:

            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root
            

            

        