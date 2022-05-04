# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        main_prev=None
        ptr=head
        prev=None
        for i in range(k):
            if not ptr:
                return head
            main_prev=ptr
            ptr=ptr.next
        main=head
        for i in range(k):
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        
        main.next=self.reverseKGroup(temp,k)
        return main_prev
