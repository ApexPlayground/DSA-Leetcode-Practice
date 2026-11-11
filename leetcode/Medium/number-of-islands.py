// Problem: Number of Islands
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/number-of-islands/
// Solved on: 2026-11-11T18:20:08.179Z

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])

        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        def dfs(r, c):

            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited or grid[r][c] == "0":
                return 
            
            visited.add((r, c))

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                dfs(nr, nc)
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        
        return count





        
        