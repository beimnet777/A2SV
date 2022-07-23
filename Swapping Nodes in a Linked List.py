# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tot=0
        ptr=head
        while ptr:
            tot+=1
            ptr=ptr.next
        target1,target2=k,tot-k+1
        node1,node2=None,None
        ptr=head
        print(target1,target2)
        for i in range(max(target1,target2)):
            if i+1==target1:
                node1=ptr
            if i+1==target2:
                node2=ptr
            ptr=ptr.next
        temp=node1.val
        node1.val=node2.val
        node2.val=temp
        return head
