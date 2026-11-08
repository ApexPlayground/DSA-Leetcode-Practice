// Problem: Insert Interval
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/insert-interval/
// Solved on: 2026-11-08T17:43:18.721Z

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        def merge(arr):
            arr.sort()

            res = [arr[0]]

            for i in range(1, len(arr)):
                start, end = arr[i]

                if start <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], end)
                else:
                    res.append([start, end])
            
            return res

        intervals.append(newInterval)

      

        return merge(intervals)

        


        