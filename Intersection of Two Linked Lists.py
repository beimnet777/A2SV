# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        j=set()
        while headA!=None or headB !=None:
            if headA !=None and headA not in j:
                j.add(headA)
                headA=headA.next
            elif headA==None:
                pass
            else:
                return headA
            if headB !=None and headB not in j:
                j.add(headB)
                headB=headB.next
            elif headB==None:
                pass
            else:
                return headB
        return None
