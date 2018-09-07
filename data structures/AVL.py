import Tree

class AVL(Tree.Tree):

    def __init__(self,data):
        super().__init__(data)
        self.height=0




def LL(root):
    W=root.left
    root.left=W.right
    W.right=root
    root.height=max(root.left.height,root.right.height)+1
    W.height=max(W.left.height,root.height)+1
    return  W


def RR(root):
    W = root.right
    root.right = W.left
    W.left = root
    root.height = max(root.right.height, root.left.height) + 1
    W.height = max(W.right.height, W.height) + 1
    return W

def LR(root):
    root.left=RR(root.left)
    return LL(root)

def RL(root):
    root.right=LL(root.right)
    return RR(root)

def Insert(root,node):
    if root is None:
        root=node
    elif node.key < root.key:
        root.left=Insert(root.left,node)

        if root.left is not None and root.right is not None and (root.left.height-root.right.height)==2:
            if node.key < root.left.key:
                root=LL(root)
            else:
                root=LR(root)

    elif node.key > root.key:
        root.right = Insert(root.right, node)
        if root.left is not None and root.right is not None and (root.right.height - root.left.height) == 2:
            if node.key < root.right.key:
                root = RR(root)
            else:
                root = RL(root)
    if (root.left is not None and root.right is not None):
        root.height=max(root.left.height,root.right.height)+1
    elif root.left is None and root.right is not None:
        root.height=root.right.height+1
    elif root.right is None and root.left is not None:
        root.height=root.left.height+1
    return root



inputs=[int(s) for s in input("please enter the list of keys : ").split()]

root = AVL(inputs[0])
for i in range(1,len(inputs)):
    Insert(root,AVL(inputs[i]))
Tree.Traversal().InOrder(root)




