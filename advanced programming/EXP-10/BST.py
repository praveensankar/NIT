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


#inorder traversal
def Display(root):
    if root is not None:
        Display(root.left)
        print(root.data,' ',end='')
        if root.left:
            print(' left: ',root.left.data,end='')
        if root.right:
            print(' right : ',root.right.data,end='')
        print()
        Display(root.right)


def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left

    return current


def Delete(root, key):
    if root is None:
        print(key," is not present in the tree ")
        return root
    if key < root.data:
        root.left = Delete(root.left, key)
    elif (key > root.data):
        root.right = Delete(root.right, key)
    else:
        # found the node and for only one child
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


def Search(root,key):
    if root is None:
        return None
    if key<root.data:
        return Search(root.left,key)
    if key>root.data:
        return Search(root.right,key)
    if key==root.data:
        return root

inputs=[int(s) for s in input("please enter the list of keys : ").split()]
root = BST(inputs[0])
for i in range(1,len(inputs)):
    Insert(root,BST(inputs[i]))
print("tree(inorder) : ")
Display(root)

while True:
    choice=int(input("please enter  1 - Insert  2 - search 3 - delete  4-display [-1 to exit] : "))
    if(choice == -1):
        break
    if choice==4:
        print("tree(inorder) : ")
        Display(root)
        continue

    key = int(input("please enter the key : "))

    if choice == 1:
        Insert(root,BST(key))
        print("tree(inorder) : ")
        Display(root)
        continue

    if  choice == 2:
        temp=Search(root,key)
        if temp is None:
            print(key," is not found")
        else:
            print(key," is found")
        continue


    if choice==3:
        root=Delete(root,key)
        print("tree(inorder) : ")
        Display(root)
        continue

