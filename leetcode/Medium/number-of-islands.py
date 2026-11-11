// Problem: Number of Islands
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/number-of-islands/
// Solved on: 2026-11-11T15:57:35.455Z

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        seen = set()

        def dfs(r, c):

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0" or (r, c) in seen:
                return 
            
            seen.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
    
        count = 0
        for x in range(row):
            for y in range(col):
                if (x, y) not in seen and grid[x][y] == "1":
                    dfs(x, y)
                    count += 1
        
        return count
        