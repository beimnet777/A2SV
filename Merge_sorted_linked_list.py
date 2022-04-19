# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val<list2.val:
                head=list1
                list1=list1.next  
            else:
                head=list2
                list2=list2.next
        elif list1:
            head=list1
            list1=list1.next
        elif list2:
            head=list2
            list2=list2.next
            
        else:
            return list1
        ans=head
            
        while list1 or list2:
            if list1 and list2:
                if list1.val<list2.val:
                    head.next=list1
                    head=head.next
                    list1=list1.next
                else:
                    head.next=list2
                    head=head.next
                    list2=list2.next
            elif list1:
                while list1:
                    head.next=list1
                    head=head.next
                    list1=list1.next
                return ans
            else:
                while list2:
                    head.next=list2
                    head=head.next
                    list2=list2.next
                return ans 
          
        return ans
            
            
        
