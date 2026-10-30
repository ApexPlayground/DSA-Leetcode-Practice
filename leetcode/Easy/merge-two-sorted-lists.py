// Problem: Merge Two Sorted Lists
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-two-sorted-lists/
// Solved on: 2026-10-30T05:13:58.310Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        curr1 = list1
        curr2 = list2

        dummy = ListNode(-1)
        prev = dummy


        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                curr2 = curr2.next
            prev = prev.next
        
        if curr1:
            prev.next = curr1
        
        if curr2:
            prev.next = curr2
        
        return dummy.next

        