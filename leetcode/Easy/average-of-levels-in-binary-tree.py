// Problem: Average of Levels in Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/
// Solved on: 2026-11-08T15:28:54.369Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:

        queue = collections.deque([root])
        res = []

        while queue:
            lvl_size = len(queue)
            total = 0

            for i in range(lvl_size):

                node = queue.popleft()

                total += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            res.append(total / lvl_size)
        
        return res




        