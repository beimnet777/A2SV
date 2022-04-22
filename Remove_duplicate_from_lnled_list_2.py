# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        removable=set()
        list1=[]
        if head:
            while head.next:
                if head.next.val==head.val:
                    removable.add(head.val)
                else:
                    list1.append(head.val)
                head=head.next
            if head.val not in removable:
                list1.append(head.val)
        list1=[i for i in list1 if i not in removable][::-1]
        prev=None
        head=None
        for i in list1:
            head=ListNode(i)
            head.next=prev
            prev=head
        return head
        
        

        
        
