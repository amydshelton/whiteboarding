class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root =  None

    def search(self, value):
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node
        return "Not Found"  


    # def r_search(self, value, node=self.root):
    #     if not node:
    #         return "Not Found"
    #     elif value < node.value:
    #         return r_search(value, node.left)
    #     elif value > node.value:
    #         return r_search(value, node.right)
    #     else:
    #         return node

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def append_node(self, value):
        new_node = Node(value)

        if not self.root:
            self.root =  new_node
        else:
            node = self.root
            while new_node.value != node.value: # this will eventually be true because you'll set the new node equal to the current node
                if new_node.value < node.value and node.left:
                    node = node.left # move into the left node
                elif new_node.value < node.value:
                    node.left = new_node
                elif new_node.value > node.value and node.right:
                    node = node.right
                elif new_node.value > node.value:
                    node.right = new_node