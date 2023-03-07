class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def search(self, value, node):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self.search(value, node.left_child)
        else:
            return self.search(value, node.right_child)

    def insert(self, value, node):
        if value < node.value:
            if node.left_child is None:
                node.left_child = TreeNode(value)
            else:
                self.insert(value, node.left_child)
        elif value > node.value:
            if node.right_child is None:
                node.right_child = TreeNode(value)
            else:
                self.insert(value, node.right_child)

    def delete(self, value, node):
        if node is None:
            return
        elif value < node.value:
            node.left_child = self.delete(value, node.left_child)
            return node
        elif value > node.value:
            node.right_child = self.delete(value, node.right_child)
            return node
        elif value == node.value:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                node.right_child = self.lift(node.right_child, node)
                return node
            
    def lift(self, node, parent):
        if node.left_child:
            node.left_child = self.lift(node.left_child, parent)
            return node
        else:
            node.value = parent.value
            return node.right_child


node_1 = TreeNode(25)
node_2 = TreeNode(75)
root = TreeNode(50, node_1, node_2)
