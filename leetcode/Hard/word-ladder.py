// Problem: Word Ladder
// Platform: leetcode
// Rating/Difficulty: Hard
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/word-ladder/
// Solved on: 2026-11-23T09:52:29.693Z

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        if endWord not in wordList:
            return 0
        
        steps = 1

        queue = collections.deque([(beginWord, steps)])
        seen = {beginWord}

        while queue:

            curr_word, curr_step = queue.popleft()

            if curr_word == endWord:
                return curr_step

            for word in wordList:

                if word in seen:
                    continue
                
                diff = 0
                for i in range(len(word)):
                    if word[i] != curr_word[i]:
                        diff += 1
                    
                    if diff > 1:
                        break
                
                if diff == 1:
                    queue.append((word, curr_step + 1))
                    seen.add(word)
        
        return 0



        