# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            new_head=head.next.next
            b=head.next
            b.next=head
            
            next_new=self.swapPairs(new_head)
            head.next=next_new
            return b
