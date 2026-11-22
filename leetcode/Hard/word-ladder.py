// Problem: Word Ladder
// Platform: leetcode
// Rating/Difficulty: Hard
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/word-ladder/
// Solved on: 2026-11-22T13:05:35.508Z

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        if endWord not in wordList:
            return 0

        queue = collections.deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:

            curr, steps = queue.popleft()

            if curr == endWord:
                return steps

            for word in wordList:
                if word in seen:
                    continue
                
                diff = 0

                for i in range(len(word)):
                    if curr[i] != word[i]:
                        diff += 1
                
                    if diff > 1:
                        break

                if diff == 1:
                    queue.append((word, steps + 1))
                    seen.add(word)
        return 0
            
                
               
                


            


        