// Problem: Keys and Rooms
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/keys-and-rooms/
// Solved on: 2026-11-12T10:33:45.950Z

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        queue = collections.deque([0])
        seen = {0}

        while queue:
            
            node = queue.popleft()

            for neig in rooms[node]:
                if neig not in seen:
                    queue.append(neig)
                    seen.add(neig)
        
        return len(seen) == len(rooms)



        