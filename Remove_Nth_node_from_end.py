# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        ans=head
        
        if head.next==None:
            return None
        for i in range(n-1):
            ptr=ptr.next
        while ptr.next:
            prev=head
            head=head.next
            ptr=ptr.next
        if head.next:
            head.val=head.next.val
            head.next=head.next.next
        else:
            prev.next=None
        
        return ans
        
