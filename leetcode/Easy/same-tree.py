// Problem: Same Tree
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/same-tree/
// Solved on: 2026-11-06T07:26:16.790Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            n1 = stack1.pop()
            n2 = stack2.pop()

            if n1 is None and n2 is None:
                continue

            if n1 is None or n2 is None:
                return False
            
            if n1.val != n2.val:
                return False
            
            stack1.append(n1.left)
            stack2.append(n2.left)
           
            stack1.append(n1.right)
            stack2.append(n2.right)

        
        return not stack1 and not stack2
        