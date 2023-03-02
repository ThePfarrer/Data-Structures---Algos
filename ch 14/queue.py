from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, data):
        self.data = DoublyLinkedList()

    def enqueue(self, element):
        self.data.insert_at_end(element)

    def dequeue(self):
        removed_node = self.data.remove_from_front()
        return removed_node.data

    def read(self):
        return None if not self.data.first_node else self.data.first_node.data
