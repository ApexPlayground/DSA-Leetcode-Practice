// Problem: Binary Tree Level Order Traversal
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
// Solved on: 2026-11-24T09:38:21.332Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        queue = collections.deque([root])
        res = []

        if not root:
            return []

        while queue:
            lvl = len(queue)
            curr = []
            for _ in range(lvl):
                node = queue.popleft()

                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            res.append(curr)
        
        return res
            

        