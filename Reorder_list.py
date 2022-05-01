# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        list1=[]
        ptr=head
        while head:
            list1.append(head)
            head=head.next
        i,j=1,len(list1)-1
        if len(list1)%2!=0:
            list1[(len(list1)//2)].next=None
        while i<=j:
            if i==j:
                node=list1[i]
                ptr.next=node
                node.next=None
            else:
                node=list1[j]
                ptr.next=node
                ptr=node
                node2=list1[i]
                ptr.next=node2
                ptr=node2
            i+=1
            j-=1       
