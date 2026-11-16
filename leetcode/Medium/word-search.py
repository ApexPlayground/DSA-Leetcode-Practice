// Problem: Word Search
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/word-search/
// Solved on: 2026-11-16T20:03:04.801Z

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        seen = set()
        def dfs(br, bc, i):
            if i == len(word):
                return True
            
            # if within bound
            if br < 0 or br >= row or bc < 0 or bc >= col or (br, bc) in seen or word[i] != board[br][bc]:
                return False
            
            seen.add((br, bc))
            res = (dfs(br + 1, bc, i + 1) or dfs(br - 1, bc, i + 1) or dfs(br, bc + 1, i + 1) or dfs(br, bc - 1, i + 1))

            # Remove the current cell from the visited set (backtracking)
            seen.remove((br, bc))

            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        
        return False
        
        