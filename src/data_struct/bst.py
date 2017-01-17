class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:

    def __init__(self):
        self.root = None

    def find(self, data, node):
        if node is None:
            return node
        elif node.data == data:
            return node
        elif data < node.data:
            return self.find(data, node.left)
        else:
            return self.find(data, node.right)

