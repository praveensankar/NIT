class BST:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def Insert(root, Node):
    if root is None:
        root = Node
    else:
        if Node.data < root.data:
            if root.left is None:
                root.left = Node
            else:
                Insert(root.left, Node)
        else:
            if root.right is None:
                root.right = Node
            else:
                Insert(root.right,Node)


def Display(root):
    if root is not None:
        Display(root.left)
        print(root.data)
        Display(root.right)


def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left

    return current


def Delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = Delete(root.left, key)
    elif (key > root.data):
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

        root.data = temp.data
        root.right = Delete(root.right, temp.data)

    return root




inputs=[int(s) for s in input("please enter the list of keys : ").split()]
root = BST(inputs[0])
for i in range(1,len(inputs)):
    Insert(root,BST(inputs[i]))
Display(root)

while True:
    key=int(input("please enter key to delete [-1 to exit] : "))
    if(key == -1):
        break
    temp=Delete(root,key)
    Display(root)