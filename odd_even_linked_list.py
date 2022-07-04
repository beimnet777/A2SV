# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        odd=head
        even=head.next
        temp1=odd
        temp2=even
        head=head.next.next
        flag=1
        while head:
            if flag==1:
                temp1.next=head
                temp1=head
                flag=0
            else:
                temp2.next=head
                temp2=head
                flag=1
            head=head.next       
        temp2.next=None
        temp1.next=None
        temp1.next=even
        return odd        
