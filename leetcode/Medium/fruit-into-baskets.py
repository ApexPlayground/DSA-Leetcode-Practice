// Problem: Fruit Into Baskets
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/fruit-into-baskets/
// Solved on: 2026-10-28T19:40:29.253Z

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {} 
        best = 0

        l = 0

        for r in range(len(fruits)):

            freq[fruits[r]] = freq.get(fruits[r], 0) + 1


            if len(freq) > 2:
                freq[fruits[l]] -= 1

                if  freq[fruits[l]] == 0:
                    del freq[fruits[l]]

                l += 1
            
            best = max(best, r - l + 1)

        return best

        