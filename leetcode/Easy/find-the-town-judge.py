// Problem: Find the Town Judge
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-the-town-judge/
// Solved on: 2026-11-12T17:39:04.889Z

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        out_degree = [0] * n
        in_degree = [0] * n

        for u, v in trust:
            out_degree[u - 1] += 1
            in_degree[v - 1] += 1
        
        for i, (give_trust, get_trust) in enumerate(zip(out_degree, in_degree)):
            if give_trust == 0 and get_trust == n - 1:
                return i + 1
      
        
        return -1

        
        