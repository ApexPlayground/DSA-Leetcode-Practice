// Problem: Shortest Path in Binary Matrix
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/
// Solved on: 2026-11-12T09:15:22.924Z

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        row = col = n
        seen = {(0, 0)}
        steps = 1
        queue = collections.deque([(0, 0)])

        directions = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]

        while queue:

            curr = len(queue)

            for _ in range(curr):
                x, y = queue.popleft()

                if (x, y) == (n-1, n-1):
                    return steps
                
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in seen and grid[nx][ny] == 0:
                        queue.append((nx, ny))
                        seen.add((nx, ny))
            
            steps += 1
        
        return -1
                




        