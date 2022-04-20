# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans=-1
        i=0
        j=-1
        list1=[]
        while head:
            list1.append(head.val)
            head=head.next
            j+=1
        while i<j:
            if ans<list1[i]+list1[j]:
                ans=list1[i]+list1[j]
            i+=1
            j-=1
        return ans
                  
