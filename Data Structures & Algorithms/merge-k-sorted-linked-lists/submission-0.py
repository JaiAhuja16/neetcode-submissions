# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            l = ListNode(0)
            dummy = l
            while l1 and l2:
                if l1.val < l2.val:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
                l = l.next
            l.next = l1 or l2
            return dummy.next
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return merge(left, right)

