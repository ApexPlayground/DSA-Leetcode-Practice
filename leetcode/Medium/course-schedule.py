// Problem: Course Schedule
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/course-schedule/
// Solved on: 2026-11-16T19:37:48.756Z

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        n = numCourses
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        print(adj)
        
        queue = deque(i for i in range(n) if indegree[i] == 0)
        print(queue)

        order = []

        while queue:
            curr = queue.popleft()
            order.append(curr)

            for neig in adj[curr]:
                indegree[neig] -= 1

                if indegree[neig] == 0:
                    queue.append(neig)
        
        print(order)
        if len(order) != n:
            return False
        
        return True


        
        