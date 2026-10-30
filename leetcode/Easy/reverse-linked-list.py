// Problem: Reverse Linked List
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/reverse-linked-list/
// Solved on: 2026-10-30T04:52:10.442Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        return prev


        