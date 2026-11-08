// Problem: Merge Intervals
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-intervals/
// Solved on: 2026-11-08T16:27:33.046Z

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()

       

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            
            start, end = intervals[i]

            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
                #res.append([curr[0], r])

            else:
                res.append([start, end])
               
        
        return res

        