// Problem: Palindrome Linked List
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/palindrome-linked-list/
// Solved on: 2026-10-30T05:41:53.206Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        half_start = slow
 
        
        second_head = self.reverselist(half_start)
        first_head = head
        

        while first_head and second_head:
            if first_head.val != second_head.val:
                return False
            first_head = first_head.next
            second_head = second_head.next
        
        return True
        

                
    
    def reverselist(self, head):
        prev = None
        curr = head

        while curr != None:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev
        