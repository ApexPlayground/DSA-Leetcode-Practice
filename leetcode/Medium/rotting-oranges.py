// Problem: Rotting Oranges
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/rotting-oranges/
// Solved on: 2026-11-12T09:43:46.867Z

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        queue = collections.deque()
        row = len(grid)
        col = len(grid[0])

        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        time = 0

        while queue and fresh > 0:
            curr = len(queue)

            for _ in range(curr):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1
                



        