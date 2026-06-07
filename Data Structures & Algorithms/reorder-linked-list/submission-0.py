# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 ---> 1 ---> 2 ---> 3 ---> 4
        # 0 -> n - 1 -> 1 -> n - 2 -> 2
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        i = 0
        j = len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            if i + 1 < j:
                arr[j].next = arr[i + 1]
            i += 1
            j -= 1
        arr[i].next = None