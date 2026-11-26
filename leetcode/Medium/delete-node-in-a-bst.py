// Problem: Delete Node in a BST
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/delete-node-in-a-bst/
// Solved on: 2026-11-26T10:31:06.791Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node, val):
            if not node:
                return None
            
            if node:
                if val < node.val:
                    node.left = helper(node.left, val)
                elif val > node.val:
                    node.right = helper(node.right, val)
                else:
                      # Node to be deleted found
                    if not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    else:
                         # Find successor (smallest in right subtree)
                        replacement = node.right
                        while replacement.left:
                            replacement = replacement.left
                         # Copy successor's value to current node
                        node.val = replacement.val

                        #delete the successor
                        node.right = helper(node.right, replacement.val)
            return node
        return helper(root, key)

        