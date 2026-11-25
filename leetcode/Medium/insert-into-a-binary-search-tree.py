// Problem: Insert into a Binary Search Tree
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/insert-into-a-binary-search-tree/
// Solved on: 2026-11-25T18:59:21.289Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node, val):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                else:
                    helper(node.left, val)
            elif val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                else:
                    helper(node.right, val)
        
        if not root:
            return TreeNode(val)

        helper(root, val) 
        return root