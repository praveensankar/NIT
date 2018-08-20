class Stack:
    """ This is the implementation of stack data structure in python"""

    
    def __init__(self,n=100):
        self.array=[]
        self.top=-1
        self.size=n

    def Push(self,data):
        try:
            if self.top<self.size:
                self.array[self.top+1:]=[data]
                self.top=self.top+1
            else:
                raise NameError
        except NameError:
            print("stack overflow")
    
    def Pop(self):
        try:
            if self.top!=-1:
                d=self.array[self.top]
                self.array[self.top:]=[]
                self.top=self.top-1
                return d
            else:
                raise NameError
        except NameError:
            print("stack Underflow")

    def Peek(self):
        try:
            if self.top!=-1:
                return self.array[self.top]
            else:
                raise NameError
        except NameError:
            print("stack undeflow")
    
    def Display(self):
        print("size : {0}\t top : {1}".format(self.size,self.top))
        for i in range(0,self.top+1):
            print(self.array[i],end=", ")
        # print(self.array[i+1])


class Test:

   
    size=0
    size=int(input("please enter the size of the stack : "))
    s=Stack(size)
    print("please enter the elements")
    for i in range(size):
        data=int(input())
        s.Push(data)
    
    while True:
        print("please enter 1 - push an element\t 2 - pop\t 3 - peek\t  4 - display stack\t 5 - exit")
        choice=int(input())
        if choice == 1:
            data=int(input("please enter the number : "))
            s.Push(data)
        elif choice == 2:
            print(s.Pop())
        elif choice == 3: 
            print(s.Peek())
        elif choice == 4: 
            print(s.Display())
        elif choice ==5:
            break
        else:
            break
            


                 