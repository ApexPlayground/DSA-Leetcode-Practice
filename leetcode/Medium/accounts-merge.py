// Problem: Accounts Merge
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/accounts-merge/
// Solved on: 2026-11-18T07:27:07.200Z

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def _add(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0
    
    def find(self, node):
        self._add(node)
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return None
        
        if self.rank[root_y] > self.rank[root_x]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_y] == self.rank[root_x]:
            self.rank[root_x] += 1

class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = defaultdict(str)
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]

            root_email = emails[0]

            res = []

            for email in emails:
                uf.union(root_email, email)
                email_to_name[email] = name
    
        email_group = defaultdict(list)
        for email in email_to_name:
            root_email = uf.find(email)
            email_group[root_email].append(email)
        
        res = []
        for root_email, email_list in email_group.items():
            user_name = email_to_name[root_email]
            user_arr = [user_name]

            user_arr.extend(sorted(email_list))
            res.append(user_arr)
        
        return res



                
      

        


        