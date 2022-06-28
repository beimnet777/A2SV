# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums=[]
        for i in lists:
            while i!=None:
                nums.append(i.val)
                i=i.next
        heapq.heapify(nums)
        if len(nums)==0:
            return None
        head=ListNode(heapq.heappop(nums))
        temp=head
        while len(nums)>0:
            node=ListNode(heapq.heappop(nums))
            temp.next=node
            temp=node
        return head            
