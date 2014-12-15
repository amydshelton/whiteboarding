
def depth_first_traversal(node):
    if node:
        # print node.value  # pre-order
        depth_first_traversal(node.left)
        print node.value # in pre-order
        depth_first_traversal(node.right)
        # print node.value # post-order
    return