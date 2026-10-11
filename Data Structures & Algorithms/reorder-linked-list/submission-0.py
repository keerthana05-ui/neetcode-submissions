# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        first = head
        second = prev
        while second:
            temp1 = first.next
            tmp = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = tmp
        