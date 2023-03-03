class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.prev = self.last_node
            self.last_node.next = new_node
            self.last_node = new_node

    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next
        return removed_node

    def print_list_in_reverse(self):
        output = ""

        current_node = self.last_node

        while current_node:
            output += "<-" + str(current_node.data)
            current_node = self.node.prev

        print(output)


double_ll = DoublyLinkedList()
