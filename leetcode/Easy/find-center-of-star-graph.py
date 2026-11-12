// Problem: Find Center of Star Graph
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-center-of-star-graph/
// Solved on: 2026-11-12T16:48:02.561Z

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        for k, v in adj.items():
            if len(v) == len(adj) - 1:
                return k
        