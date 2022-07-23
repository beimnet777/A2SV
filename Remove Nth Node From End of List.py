# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        ans=head
        ctr=0
        if head.next==None:
            return None
        while ptr:
            ptr=ptr.next
            ctr+=1
        x=ctr-n
        ptr=head
        for i in range(x-1):
            ptr=ptr.next
        if x<=0 :
            return head.next
        ptr.next=ptr.next.next
        return head
        
#         if head.next==None:
#             return None
#         for i in range(x-1):
#             ptr=ptr.next
#         while ptr.next:
#             prev=head
#             head=head.next
#             ptr=ptr.next
#         if head.next:
#             head.val=head.next.val
#             head.next=head.next.next
#         else:
#             prev.next=None
        
#         return ans
      
