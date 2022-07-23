# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr=[]
        ptr=head
        while head:
            arr.append(head.val)
            head=head.next
        target=-1
        for j,i in enumerate(arr):
            if i>=x:
                target=j
                break
        # print(arr,target)
        if target==-1 or target==len(arr)-1:
            return ptr
        ctr=0
        while ctr<len(arr):
            if arr[ctr]<x and ctr>target:
                # print(ctr,target)
                i=arr.pop(ctr)
                arr.insert(target,i)
                target+=1
            ctr+=1
        head=ListNode(arr[0])
        ptr=head
        ctr=1
        while ctr<len(arr):
            node=ListNode(arr[ctr])
            ptr.next=node
            ptr=node
            ctr+=1
                
        return head
