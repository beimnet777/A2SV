# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        if not head.next.next:
            head.next=None
            return head
        ptr=head
        ptr2=head.next
        while ptr2:
            if ptr2.next:
                ptr2=ptr2.next.next
                ptr=ptr.next
            else:
                ptr=ptr.next
                break
        ptr.val=ptr.next.val
        ptr.next=ptr.next.next
        return head  
