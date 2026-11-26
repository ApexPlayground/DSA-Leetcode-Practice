// Problem: Binary Tree Level Order Traversal
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
// Solved on: 2026-11-26T11:00:17.666Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            lvl = len(queue)
            lvl_arr = []

            for _ in range(lvl):
                node = queue.popleft()
                lvl_arr.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(lvl_arr)
        return result

        