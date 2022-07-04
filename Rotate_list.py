# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        li=deque()
        while head !=None:
            li.append(head.val)
            head=head.next
        for i in range(k%len(li)):
            li.appendleft(li.pop())
        head =ListNode(li[0])
        temp=head
        l=1
        while l<len(li):
            node=ListNode(li[l])
            temp.next=node
            temp=node
            l+=1
        return head
            
