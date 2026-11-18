// Problem: LRU Cache
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/lru-cache/
// Solved on: 2026-11-18T07:12:09.258Z

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None  


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        # head, tail
        self.least_used = ListNode(0, 0)
        self.most_used = ListNode(0, 0)

        # link together 
        self.least_used.next = self.most_used
        self.most_used.prev = self.least_used
         
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.most_used.prev
        prev.next = node
        node.prev = prev
        node.next = self.most_used
        self.most_used.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return - 1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        else:
            if len(self.cache) >=  self.capacity:
                lru = self.least_used.next
                self.remove(lru)
                del self.cache[lru.key]
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
    



           
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)