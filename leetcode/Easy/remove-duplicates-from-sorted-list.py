// Problem: Remove Duplicates from Sorted List
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
// Solved on: 2026-10-30T05:32:20.485Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        seen = set()

        dummy = ListNode(-1)
        prev = dummy

        curr = head

        while curr:

            if curr.val in seen:
                prev.next = curr.next
                curr = curr.next
            else:
                seen.add(curr.val)

                prev.next = curr
                prev = curr
                curr = curr.next
                
        return dummy.next

        