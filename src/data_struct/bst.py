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
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            cur = self.root
            parent = None

            while(1):
                parent = cur

                if data < parent.data:
                    current = current.left
                
                    if current is None:
                        parent.left = Node(data)
                        return
                else:
                    current = current.right

                    if current is None:
                        parent.right = Node(data)
                        return

if __name__ == '__main__':
    tree = BST()
    print(tree.root)
    tree.insert("Basic") 
