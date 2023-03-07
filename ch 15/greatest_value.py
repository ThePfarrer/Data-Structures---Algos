def greatest_value_bst(node):
    # if node is None:
    #     return None
    if node.right is None:
        return node.val
    else:
        greatest_value_bst(node.right)
    