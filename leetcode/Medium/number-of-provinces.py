// Problem: Number of Provinces
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/number-of-provinces/
// Solved on: 2026-11-13T20:13:37.127Z

class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def add(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0
    
    def find(self, node):
        self.add(node)

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return None
        
        if self.rank[root2] > self.rank[root1]:
            root1, root2 = root2, root1
        
        self.parent[root2] = root1

        if self.rank[root2] == self.rank[root1]:
            self.rank[root1] += 1
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        uf = DSU()
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        roots = set()

        for i in range(n):
            parents = uf.find(i)
            roots.add(parents)
        
        print(roots)
        return len(roots)



        