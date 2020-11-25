from typing import List
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow_ptr = head
        fast_ptr = head.next
        
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        second_list = slow_ptr.next
        slow_ptr.next = None
        
        left = self.sortList(head)
        right = self.sortList(second_list)
        
        if not left or not right:
            return left or right
        
        if left.val > right.val:
            left,right = right, left
        head = pre = left
        left = left.next
        while left and right:
            if left.val < right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next
        pre.next = left or right # concatenate the longer list that is leftover
        return head


