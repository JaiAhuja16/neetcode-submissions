# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = ListNode(head.val)
            while head.next:
                L = ListNode(head.next.val)
                L.next = curr
                curr = L
                head = head.next
            return curr