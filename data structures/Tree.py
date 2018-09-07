class Tree:

    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

class Traversal:

    def InOrder(self,root):
        if root is not None:
            self.InOrder(root.left)
            print(root.key)
            self.InOrder(root.right)



