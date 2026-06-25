# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        prev_remove = head
        for _ in range(n):
            head = head.next
        
        if not head:
            return dummy.next
        
        while head.next:
            head = head.next
            prev_remove = prev_remove.next
        
        prev_remove.next = prev_remove.next.next
        return dummy