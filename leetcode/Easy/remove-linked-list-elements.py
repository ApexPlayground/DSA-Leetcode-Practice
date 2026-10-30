// Problem: Remove Linked List Elements
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/remove-linked-list-elements/
// Solved on: 2026-10-30T05:27:57.926Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:

        if not head:
            return None
        
        curr = head
        dummy = ListNode(-1)
        prev = dummy

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                

                prev.next = curr
                prev = curr
                curr = curr.next
        
        return dummy.next


        