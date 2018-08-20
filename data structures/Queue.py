class Queue:
    """ This is the implementation of queue data structure in python"""

  
    def __init__(self,n=100):
        self.array=[]
        self.size=n
        self.front=-1
        self.rear=0

    def EnQueue(self,data):
        try:
            if self.rear!=self.size:
                self.array[self.rear:self.rear+1]=[data]
                self.rear=self.rear+1
                if self.front==-1:
                    self.front=0    
            else:
                raise NameError
        except NameError:
            print("Queue overflow")
    
    def DeQueue(self):
        try:
            if self.front!=-1:
                d=self.array[self.front]
                self.array[self.front:self.front+1]=[-1]

                if self.front==self.rear-1:
                    self.front=-1
                    self.rear=0
                else:
                    self.front=self.front+1

                return d
            else:
                raise NameError
        except NameError:
            print("queue Underflow")

    
    
    def Display(self):
        print("size : {0}\t front : {1}\t rear : {2}".format(self.rear-self.front,self.front,self.rear))
        for i in range(self.front,self.rear):
            if self.array[i]!=-1:
                print(self.array[i],end=", ")
    

class Test:

   
    size=0
    size=int(input("please enter the size of the queue : "))
    q=Queue(size)
    print("please enter the elements")
    for i in range(size):
        data=int(input())
        q.EnQueue(data)
    
    while True:
        print("please enter 1 - Add an element\t 2 - Delete an element\t  3 - display queue\t 4 - exit")
        choice=int(input())
        if choice == 1:
            data=int(input("please enter the number : "))
            q.EnQueue(data)
        elif choice == 2:
            print(q.DeQueue())
        elif choice == 3: 
            print(q.Display())
        elif choice ==4:
            break
        else:
            break
            


                 