// Problem: Rotting Oranges
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/rotting-oranges/
// Solved on: 2026-11-12T09:01:55.253Z

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
       

        queue = deque()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        while queue and fresh:
            stage = len(queue)

            while stage:
            
                sr, sc = queue.popleft()

                for dr, dc in dir:
                    nr, nc = sr + dr, sc + dc

                    if (0 <= nr < row) and (0 <= nc < col) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
                stage -= 1

            time += 1
                    
        return time if fresh == 0 else -1
        



        