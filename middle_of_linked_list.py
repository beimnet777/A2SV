# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m_node=head
        counter=0
        while(head):
            counter+=1
            head=head.next
        if counter%2==0:
            middle=  (counter/2)+1
        else:
            middle= (counter//2)+1
                
        print(middle)
        for i in range(int(middle)-1):
            m_node=m_node.next
        return m_node
            
            
        
