// Problem: Count Good Nodes in Binary Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
// Solved on: 2026-11-26T11:48:56.457Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
       

        def dfs(node, max_seen):
            nonlocal count

            if not node:
                return
            
            if node.val >= max_seen:
                count += 1
                max_seen = node.val
            
            dfs(node.left, max_seen)
            dfs(node.right, max_seen)
        
        dfs(root,  float('-inf'))

        return count


        