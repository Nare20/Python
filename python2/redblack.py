class Node:
    def __init__(self,key = "None",color = "black"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.Nil = Node(key = 'None', color = 'Black')
        self.root = self.Nil

