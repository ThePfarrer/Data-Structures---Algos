class Node:

    def __init__(self, data, next=None):
        self.data = data


class LinkedList:

    def __init__(self, node):
        self.node = node

    def read(self, index):
        current_node = self.node
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

            if current_node is None:
                break

        return current_node.data

    def index_of(self, value):
        current_node = self.node
        current_index = 0

        while True:
            if current_node.data == value:
                return current_index

            current_node = current_node.next
            current_index += 1

            if current_node is None:
                break

        return None

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.node

            self.node = new_node
            return

        current_node = self.node
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def delete_at_index(self, index):

        if index == 0:
            self.node = self.node.next
            return

        current_node = self.node
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        current_node.next = current_node.next.next

    def print_list(self):
        output = ""

        while self.node is not None:
            output += str(self.node.data) + "->"
            self.node = self.node.next

        print(output)

    def last_element(self):
        current_node = self.node

        while current_node:
            current_node = current_node.next

            if current_node.next is None:
                return current_node.data
