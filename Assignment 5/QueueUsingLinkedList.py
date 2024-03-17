class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        while current:
            print(current.key, end=' ')
            current = current.next
        print()

    def Enqueue(self, x):
        x = Node(x)
        node = None
        if self.head == None:
            self.head = x
        else:
            node = self.tail
            node.next = x
        x.next = None
        self.tail = x
    
    def Dequeue(self):
        if self.head == None:
            return "Queue Underflow"
        node = self.head.next
        delNode = self.head
        if self.head == self.tail:
            self.tail = None
        self.head = node
        delNode.next = None
        return delNode.key

if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.Enqueue(1)
    linked_list.Enqueue(2)
    linked_list.Enqueue(3)
    print(linked_list.Dequeue())
    print(linked_list.Dequeue())
    print(linked_list.Dequeue())
    print(linked_list.Dequeue())
