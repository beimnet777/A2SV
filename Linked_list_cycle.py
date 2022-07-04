# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None :return None
        ptr=head.next
        while ptr and ptr.next and ptr.next.next:
            if head==ptr:
                return True
            else:
                head=head.next
                ptr=ptr.next.next
        return False
