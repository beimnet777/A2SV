class Node:
    def __init__(self,val,nextNode=None):
        self.val=val
        self.next=nextNode
class MyLinkedList:

    def __init__(self):
        self.head=None
        
    def get(self, index: int) -> int:
        j=0
        head=self.head
        if head:
            while head.next:
                if j==index:
                    break
                head=head.next
                j+=1
            if index>j:
                return -1
            
            return head.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if self.head:
            temp=self.head
            self.head=Node(val)
            self.head.next=temp
        else:
            self.head=Node(val)
        
    def addAtTail(self, val: int) -> None:
        if self.head==None:
            self.head=Node(val)
        else:
            head=self.head
            while head.next:
                head=head.next
            head.next=Node(val)
            
    def addAtIndex(self, index: int, val: int) -> None:
        head=self.head
        j=0
        if head:
            while head:
                if j==index:
                    break
                j+=1
                head=head.next

        if index>j:
            return
        if j==0:
            self.addAtHead(val)
            return
        if head==None:
            self.addAtTail(val)
        else:
            temp,temp_val=head.next,head.val
            head.val=val
            head.next=Node(temp_val,temp)

    def deleteAtIndex(self, index: int) -> None:
        head=self.head
        j=0
        prev=None
        if head:
            while head.next:
                if j==index:
                    break
                j+=1
                prev=head
                head=head.next
   
        if index>j:
            return
        
        if prev:
            prev.next=head.next
 
        elif head:
            self.head=head.next
        else:
            return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
