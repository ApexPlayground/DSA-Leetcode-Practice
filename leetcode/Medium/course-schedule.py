// Problem: Course Schedule
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/course-schedule/
// Solved on: 2026-11-22T13:24:26.696Z

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n = numCourses

        adj = defaultdict(list)
        indegree = [0] * n

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        queue = collections.deque()

        for course, req in enumerate(indegree):
            if req == 0:
                queue.append(course)
        
        print(queue)
        
        order = 0
        while queue:
            curr_course = queue.popleft()
            order += 1

            for neig in adj[curr_course]:
                indegree[neig] -= 1

                if indegree[neig] == 0:
                    queue.append(neig)
        
        return order == n




        