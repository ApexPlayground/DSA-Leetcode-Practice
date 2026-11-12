// Problem: Number of Provinces
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/number-of-provinces/
// Solved on: 2026-11-12T10:38:04.163Z

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        seen = set()
        cities = len(isConnected)

        col = len(isConnected[0])


        def dfs(city):
            if city in seen:
                return
            
            seen.add(city)

            for neig in range(cities):
                if isConnected[city][neig] == 1:
                    dfs(neig)
        
        count = 0
        for city in range(cities):
            if city not in seen:
                dfs(city)

                count += 1
        
        return count
            


        
        