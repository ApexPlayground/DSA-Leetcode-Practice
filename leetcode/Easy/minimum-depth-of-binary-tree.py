// Problem: Minimum Depth of Binary Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
// Solved on: 2026-11-08T11:41:24.822Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        queue = collections.deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if node.left:
                queue.append((node.left, depth + 1))
            
            if node.right:
                queue.append((node.right, depth + 1))
            
            if not node.left and not node.right:
                return depth
        
        


        

        