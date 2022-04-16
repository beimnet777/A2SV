# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num3=[]
        num1=[]
        while l1:
            num1.append(str(l1.val))
            l1=l1.next
        num2=[]
        while l2:
            num2.append(str(l2.val))
            l2=l2.next
        num1=num1[::-1]
        num2=num2[::-1]
        
        x=int("".join(num1))+int("".join(num2))
        
        for i in str(x)[::-1]:
            num3.append(ListNode(int(i)))
        for i in range(len(num3)-1):
            num3[i].next=num3[i+1]
        return num3[0]
        
