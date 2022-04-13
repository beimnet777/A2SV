# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        while head!=None and head.next!=None:
            head=head.next.next
            p1=p1.next
        return p1
        
            
            
        
