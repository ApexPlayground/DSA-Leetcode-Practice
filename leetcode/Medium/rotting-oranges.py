// Problem: Rotting Oranges
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/rotting-oranges/
// Solved on: 2026-11-22T12:14:06.798Z

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        queue = collections.deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        while queue and fresh > 0:
            lvl = len(queue)

            for _ in range(lvl):

                x, y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1

                






        