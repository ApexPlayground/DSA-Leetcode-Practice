// Problem: Delete Node in a BST
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/delete-node-in-a-bst/
// Solved on: 2026-11-26T10:50:57.907Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def dfs(node):
            if not node:
                return None

            if key < node.val:
                node.left = dfs(node.left)
            
            elif key > node.val:
                node.right = dfs(node.right)
            
            else:

                # has no left child, relace with right
                if not node.left:
                    return node.right
                
                # has no right child
                if not node.right:
                    return node.left
                
                # has 2 kids
                curr = node.right

                # Find the leftmost node in the replacement subtree
                while curr.left:
                    curr = curr.left
                
                # Attach the original left subtree to preserve it
                curr.left = node.left

                return node.right
                
            return node
        
        return dfs(root)


        
        return dfs(root)




        