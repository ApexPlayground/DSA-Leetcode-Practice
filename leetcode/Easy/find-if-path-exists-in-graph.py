// Problem: Find if Path Exists in Graph
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-if-path-exists-in-graph/
// Solved on: 2026-11-12T10:14:51.449Z

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()

        def dfs(node):

            if node in seen:
                return
            
            seen.add(node)

            if node == destination:
                return True
            
            for neig in adj[node]:
                if dfs(neig):
                    return True
        
            return False
        
        return dfs(source)
            

        