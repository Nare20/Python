
class Node:
    def  __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def  __init__(self):
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root,key)
    def _insert_recursive(self,current,key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left,key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right,key)
        else:
            print(key)
    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, current, level):
        if current is not None:
            self._print_tree(current.right, level + 1)
            print("    " * level + str(current.key))
            self._print_tree(current.left, level + 1)


bst = BST()

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)

bst.print_tree()



        