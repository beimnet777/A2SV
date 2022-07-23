# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li=[]
        while head!=None:
            li.append(head.val)
            head=head.next
        x=li[:left-1]
        for i in range(right-1,left-2,-1):
            x.append(li[i])
        x+=li[right:]
        head=ListNode(x[0])
        ptr=head
        for i in range(1,len(x)):
            node=ListNode(x[i])
            ptr.next=node
            ptr=node
        return head 
