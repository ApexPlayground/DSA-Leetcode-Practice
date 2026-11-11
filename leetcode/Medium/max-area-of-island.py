// Problem: Max Area of Island
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/max-area-of-island/
// Solved on: 2026-11-11T20:25:04.623Z

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        seen = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   

        def dfs(r, c):

            nonlocal area

            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in seen or grid[r][c] == 0:
                return 

            seen.add((r, c))

            area += 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc  

                dfs(nr, nc)
            
            
        
            

        best = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in seen:
                    area = 0
                    dfs(i, j)
                    best = max(best, area)

        return best   
                
                


        