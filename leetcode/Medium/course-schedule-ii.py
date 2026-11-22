// Problem: Course Schedule II
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/course-schedule-ii/
// Solved on: 2026-11-22T14:37:00.805Z

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        n = numCourses
        adj = defaultdict(list)
        indegree = [0] * n

        for course, req in prerequisites:
            adj[req].append(course)
            indegree[course] += 1
        
        queue = collections.deque()

        for course, req_num in enumerate(indegree):
            if req_num == 0:
                queue.append(course)
        
        print(f"{adj}, {indegree}")
        res = []

        while queue:
            curr_course = queue.popleft()
            res.append(curr_course)

            for neig in adj[curr_course]:
                indegree[neig] -= 1

                if indegree[neig] == 0:
                    queue.append(neig)
        
        return res if len(res) == n else []


        