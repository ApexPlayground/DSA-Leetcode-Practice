// Problem: Find Smallest Letter Greater Than Target
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
// Solved on: 2026-11-02T19:33:53.883Z

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        l = 0
        r = len(letters) - 1

        while l < r:
            mid = (l + r) // 2

            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                r = mid
        
        return letters[r] if ord(letters[r]) > ord(target) else letters[0]

        