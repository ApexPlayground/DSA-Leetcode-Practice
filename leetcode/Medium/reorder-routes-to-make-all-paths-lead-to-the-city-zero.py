// Problem: Reorder Routes to Make All Paths Lead to the City Zero
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
// Solved on: 2026-11-12T19:31:50.552Z

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        adj = [[] for _ in range(n)]
       

        for u, v in connections:
            adj[v].append((u, 0))
            adj[u].append((v, 1))
        
        seen = {0}
        queue = collections.deque([0])
        total = 0

        while queue:
            node = queue.popleft()

            for neighbour, change in adj[node]:
                if neighbour not in seen:
                    queue.append(neighbour)
                    seen.add(neighbour)
                    total += change
        
        return total

        

        
      




        
        