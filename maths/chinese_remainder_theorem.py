import egcd

class Chinese_remainder_theorem:


    #  n - no of equations
    # x = (triple  - (cogruent)) a1 ( mod m1) , x=a2(mod m2)...x=an(mod mn)
    def __init__(self):
        self.n=0
        self.x=0
        self.a=[]
        self.m=[]
        self.M=[]
        self.MM=[]
        self.y=[]

    
    def GetData(self):
        self.n = int(input("Enter no of equations : "))

        print("please enter {0} equations in the format x = a1 mod m1,x=a2 mod m2,..x=an mod mn".format(self.n))
        for i in range(self.n):
            print("please a,m for {0}th equation  : ".format(i))
            self.temp_a = int(input(""))
            self.temp_m=int(input(""))
            self.a.append(self.temp_a)
            self.m.append(self.temp_m)
        
        #print(self.x,self.a,self.m)
    
    def Start(self):
        self.GetData()
        # M - multiplies all the module m
        M=1
        for i in range(self.n):
            M=M*self.m[i]

        # MM - M/Mi(i=1,2,..n)
        MM=[]
        for i in range(self.n):
            MM.append(M//self.m[i])
        
        # Y - inverse of MM(1..n) module M(1...n)
        Y=[]
        for i in range(self.n):
            temp_y=egcd.egcd(MM[i],self.m[i])
            Y.append(temp_y[1])
        
        # returns x
        x=0
        for i in range(self.n):
            x=x+(self.a[i]*MM[i]*Y[i])
        
        self.x=x
        self.MM=MM
        self.M=M
        self.y=Y
        




c=Chinese_remainder_theorem()
c.Start()
print("x = {0}\nM = {1}\nMi(i=1..n) = {2}\nyi(i=1...n) = {3}".format(c.x,c.M,c.MM,c.y))

