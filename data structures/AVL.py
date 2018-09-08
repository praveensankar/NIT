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

def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left

    return current


def Delete(root, key):

    #1 - standard BST deletion
    if root is None:
        return root
    if key < root.key:
        root.left = Delete(root.left, key)
    elif (key > root.key):
        root.right = Delete(root.right, key)
    else:
        # for only one child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #for 2 children
        temp = minValueNode(root.right)

        root.key = temp.key
        root.right = Delete(root.right, temp.key)

    # if tree has only one node
    if root is None:
        return None

    #2 - update height of the current node
    root.height=max(root.left.height,root.right.height)+1

    #3 - balance factor
    balance_factor=root.left.height-root.right.height

    if balance_factor > 1:
        if root.left.left.height - root.left.right.height >= 0:
            return LL(root)
        else:
            return LR(root)

    elif balance_factor < -1:
        if root.right.left.height - root.right.right.height <= 0:
            return RR(root)
        else:
            return RL(root)


inputs=[int(s) for s in input("please enter the list of keys : ").split()]

root = AVL(inputs[0])
for i in range(1,len(inputs)):
    Insert(root,AVL(inputs[i]))
Tree.Traversal().InOrder(root)


while True:
    key=int(input("please enter key to delete [-1 to exit] : "))
    if(key == -1):
        break
    temp=Delete(root,key)
    Tree.Traversal().InOrder(root)




