// Problem: Palindrome Linked List
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/palindrome-linked-list/
// Solved on: 2026-10-30T05:49:48.368Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        arr = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

        