// Problem: Non-overlapping Intervals
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/non-overlapping-intervals/
// Solved on: 2026-11-09T19:29:48.134Z

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """ Ok for this, i detect  overlapping intervals normally, but when updating the previus 
        interval, i check if the prev i slonger than the curr, if it is, it is potentially going
        to extend in the future and overlap with more intervals, so i get rid of if now
        """
        intervals.sort()

        print(intervals)

        prev = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev[1]:
                count += 1

                if end < prev[1]:
                    prev = [start, end]

                continue

            prev = [start, end]
        
        return count
            

            

        