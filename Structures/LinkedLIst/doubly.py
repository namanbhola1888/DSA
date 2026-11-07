class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp


    def delete_node(self, key):
        if self.head is None:
            return 

        if self.head.data == key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        temp = self.head

        while temp.next and temp.data != key:
            temp = temp.next

        if temp is None:
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next


    def search_node(self, key):
        if self.head is None:
            return

        temp = self.head
        index = 0

        while temp:
            if temp.data == key:
                return index
            
            temp = temp.next
            index += 1

        return -1


