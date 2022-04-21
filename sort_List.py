# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        while head:
            list1.append(head.val)
            head=head.next
        list1.sort(reverse=True)
        prev=None
        node=None
        for i in list1:
            node=ListNode(i,prev)
            prev=node
        return node
        
        
