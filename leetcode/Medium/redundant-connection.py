// Problem: Redundant Connection
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/redundant-connection/
// Solved on: 2026-11-13T21:12:54.526Z

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        print(parent)
        
        ans = []
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

          

            if root_x == root_y:
                ans.append([x, y])

            parent[root_y] = root_x
        
        for u, v in edges:
            union(u, v)

        return ans[-1]


        