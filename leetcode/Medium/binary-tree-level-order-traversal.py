// Problem: Binary Tree Level Order Traversal
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
// Solved on: 2026-11-08T15:32:03.030Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            lvl_size = len(queue)
            curr = []

            for i in range(lvl_size):

                node = queue.popleft()

                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            res.append(curr)
        
        return res

            



        