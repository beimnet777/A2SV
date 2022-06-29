# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num=[]
        while head:
            num.append(head.val)
            head=head.next
        ctr=1
        while ctr<len(num):
            x=ctr
            while x>0:
                if num[x]<num[x-1]:
                    num[x],num[x-1]=num[x-1],num[x]
                    x-=1
                else:
                    break
            ctr+=1
        head=ListNode(num[0])
        temp=head
        for i in range(1,len(num)):
            node=ListNode(num[i])
            temp.next=node
            temp=node
        return head        
