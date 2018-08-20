class LinkedList:
    """This is the LinkedList implementation"""
    def __init__(self):
        self._data=-1
        self._next=None
    
    def Insert(self,position,data):
        
        #temp is used to move the head pointer to the corresponding location
        temp=0

        #head is the temporary pointer of the list
        head=self

        _newNode=LinkedList()
        _newNode._data=data
        
        try:
            while temp<position:
                head=head._next
                temp=temp+1
        except:
            print("position exceeds the size of the list")
            return
        _newNode._next=head._next
        head._next=_newNode
      
    def Size(self):
        count=0
        temp=self
        temp=temp._next
        while temp!=None:
            count=count+1
            temp=temp._next
        return count


    def Delete(self,position):
        temp=0
        if position>self.Size():
            print("please enter the valid position ")
            return
        prev=self
        nex=self._next

        while temp<position:
            prev=nex
            nex=nex._next
            temp=temp+1

        prev._next=nex._next
        nex=None


    def Display(self):
        temp=self
        temp=temp._next
        while temp._next!=None:
            print(temp._data,end=", ")
            temp=temp._next
        print(temp._data)
    

class Test:

    data=[1,2,3]

    List = LinkedList()
    for i in range(len(data)):
        List.Insert(0,data[i])
    
    while True:
        print("Please Enter 1 - Insert an element\t 2 - Delete an element\t 3 - Display the List\t 4 - size of the list\t 5-exit")
        choice = int(input())
        if choice==1:
            data=int(input("please enter the data : "))
            position=int(input("please enter the position(1-first node) : "))
            List.Insert(position-1,data)
        elif choice==2:
            position=int(input("please enter the position(1-first node) : "))
            List.Delete(position-1)
            
        elif choice==3:
            List.Display()
        elif choice==4:
            print("Size of the list is ",List.Size())
        elif  choice==5:
            break