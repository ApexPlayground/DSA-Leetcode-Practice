// Problem: Word Search
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/word-search/
// Solved on: 2026-11-16T20:23:31.276Z

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])

        seen = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in seen or board[r][c] != word[i]:
                return False
            
            seen.add((r, c))

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if dfs(nr, nc, i + 1):
                    return True

            seen.remove((r, c))

            return False
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        
        return False
        