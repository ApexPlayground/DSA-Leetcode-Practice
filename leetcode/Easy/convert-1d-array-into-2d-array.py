// Problem: Convert 1D Array Into 2D Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/convert-1d-array-into-2d-array/
// Solved on: 2026-11-09T20:07:47.403Z

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if (m * n) != len(original):
            return []
        
        res = []
        for i in range(0, len(original), n):
            col = original[i : i + n]
            res.append(col)
        
        return res

        