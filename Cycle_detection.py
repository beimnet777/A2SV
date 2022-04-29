class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node


def has_cycle(head):
    if head.next:
        ptr=head.next
    else:
        return 0
    
    while head:
        if ptr==head:
            return 1
        else:
            if ptr and ptr.next and ptr.next.next:
                ptr=ptr.next.next
                head=head.next
            else:
                return 0
    return 0

