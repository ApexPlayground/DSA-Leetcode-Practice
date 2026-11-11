// Problem: Pacific Atlantic Water Flow
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
// Solved on: 2026-11-11T17:04:43.989Z

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row = len(heights)
        col = len(heights[0])

        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()

        pacific = set()
        atlantic = set()


        for i in range(row):
            for j in range(col):
                # build pacific
                if i == 0 or j == 0:
                    pacific_queue.append((i, j))
                    pacific.add((i, j))
                    
                #build atlantic
                if (i == row - 1) or (j == col - 1):
                    atlantic_queue.append((i, j))
                    atlantic.add((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(queue, seen):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen and heights[r][c] <= heights[nr][nc]:
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            
            return seen
        
        bfs(atlantic_queue, atlantic)
        bfs(pacific_queue, pacific )

        return list(atlantic & pacific)




                


        