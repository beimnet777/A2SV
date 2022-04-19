# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length=self.length(head)
        if head.next==None:
            return [0]
        i=0
        list1=[(head.val,i)]
        head=head.next
        ans=[0]*length
        while head:
            i+=1
            if list1[-1][0]>=head.val:
                list1.append((head.val,i))
                head=head.next
            else:
                while list1[-1][0]<head.val:
                    val,index=list1.pop()
                    ans[index]=head.val
                    
                    if len(list1)==0:
                        break
                list1.append((head.val,i))
                head=head.next
        return ans
    def length(self,Node):
        j=0
        while Node:
            j+=1
            Node=Node.next
        return j

        
