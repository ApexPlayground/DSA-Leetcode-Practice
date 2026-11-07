// Problem: Merge Two Binary Trees
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-two-binary-trees/
// Solved on: 2026-11-07T11:17:51.181Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:

        if not root1 and not root2:
            return None

        merged = TreeNode()

        def dfs(node1, node2, merged):
            if not node1 and not node2:
                return
            
            if node1 and node2:
                merged.val = node1.val + node2.val

            elif node1 and not node2:
                merged.val = node1.val
            
            elif node2 and not node1:
                merged.val = node2.val
            
            left1 = node1.left if node1 else None
            left2 = node2.left if node2 else None

            right1 = node1.right if node1 else None
            right2 = node2.right if node2 else None


            if left1 or left2:
                merged.left = TreeNode()
                dfs(left1, left2, merged.left)
            
            if right1 or right2:
                merged.right = TreeNode()
                dfs(right1, right2, merged.right)
        
        dfs(root1, root2, merged)
        
        return merged
        



        