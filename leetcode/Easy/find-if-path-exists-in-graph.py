// Problem: Find if Path Exists in Graph
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-if-path-exists-in-graph/
// Solved on: 2026-11-12T10:08:59.145Z

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # convert edge list to adj list

        graph = [[] for _ in range(n)]
        seen = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            if node in seen:
                return False
            
            seen.add(node)
            
            if node == destination:
                return True
        
            for neig in graph[node]:
                if dfs(neig):
                    return True
            
            return False
        return dfs(source)

                 

        
    
