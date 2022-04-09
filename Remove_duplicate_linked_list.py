# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        main=head
        while head.next:
            if head.val==head.next.val:
                head.next=head.next.next
                continue
            head=head.next
        return main
        
                
        
