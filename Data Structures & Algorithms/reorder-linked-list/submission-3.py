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
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None  # Split the list into two halves
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # PHASE 3: Interleave the two halves
        first = head
        second = prev  # 'prev' is the head of the reversed second half
        
        while second:
            # Save the next nodes so we don't lose them
            tmp1 = first.next
            tmp2 = second.next
            
            # Interleave
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2
        