// Problem: Binary Tree Right Side View
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-tree-right-side-view/
// Solved on: 2026-11-26T11:07:45.574Z

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []
        
        res = []
        queue = collections.deque([root])

        while queue:

            lvl = len(queue)
            res.append(queue[-1].val)

            for _ in range(lvl):
                node = queue.popleft()
                

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return res
        