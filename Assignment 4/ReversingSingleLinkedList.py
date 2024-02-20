class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def reverse(self):
        Currentprev = None
        Currentnext = None
        node = self.head
        CurrentHead = self.head
        while node != None:
            Currentnext = node.next
            node.next = Currentprev
            Currentprev = node
            node = Currentnext
        self.head = Currentprev
        self.tail = CurrentHead

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.tail = last_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None
        self.tail = prev

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
        print("Head: ", self.head.data)
        print("Tail: ", self.tail.data)

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    linked_list.print_list()

    linked_list.reverse()
    linked_list.print_list()
