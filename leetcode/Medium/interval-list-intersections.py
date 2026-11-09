// Problem: Interval List Intersections
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/interval-list-intersections/
// Solved on: 2026-11-09T19:53:09.367Z

class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:

        if not firstList or not secondList:
            return []
        
        i = 0
        j = 0

        res = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            max_start = max(start1, start2)
            min_end = min(end1, end2)

            if max_start <= min_end:
                res.append([max_start, min_end])

            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return res


        