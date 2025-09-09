class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def getHeight(self):
        #Calculate the total number of nodes in the BST.
        return self._getHeight(self.root)

    def _getHeight(self, node):
        if node is None:
            return 0
        return 1 + self._getHeight(node.left) + self._getHeight(node.right)

# Example usage
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("Length of BST:", bst.getHeight())