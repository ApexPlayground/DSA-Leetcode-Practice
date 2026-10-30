// Problem: Middle of the Linked List
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/middle-of-the-linked-list/
// Solved on: 2026-10-30T04:54:20.946Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        slow = head 
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        return slow

        
        