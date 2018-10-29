count=0
count_of_each_number={}
count_of_each_technique={}
fib_series={}
#normal recursion
def fib(n):

    counter()
    print("fib({0})".format(n),end=" + ")
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)


def print_series():
    global  fib_series
    global  count,count_of_each_number
    for k,v in fib_series.items():
        print(k," : ",v,end = " , ")
    print("\ncomplexity : ", count)
    for k, v in count_of_each_number.items():
        print("fib({0}) is called {1} times ".format(k, v))
    count = 0
    fib_series = {}
    count_of_each_number = {}

def counter():

    #increment the total count
    global count
    count=count+1

    #count how many times each number is called
    global  count_of_each_number
    if n in count_of_each_number:
        count_of_each_number[n]=count_of_each_number[n]+1
    else:
        count_of_each_number[n]=1

def normal_recursion(n):
    global  fib_series
    print("fib(", n, ") = ", end=" ")
    fib_series[n]=fib(n)
    print()

    global count
    count_of_each_technique['normal_recursion']=count
    print_series()

def top_down(n):
    global fib_series
    print("fib(", n, ") = ", end=" ")
    top_down_fib(n)
    print()


    global count
    count_of_each_technique['top_down']=count

    print_series()

def top_down_fib(n):
    global  fib_series
    counter()
    print("fib({0})".format(n),end=" + ")
    if n==0:
        fib_series[0]=0
        return  0
    if n==1:
        fib_series[1]=1
        return 1

    if n in fib_series:
        return fib_series[n]
    fib_series[n]=top_down_fib(n-1)+top_down_fib(n-2)
    return  fib_series[n]



def bottom_up(n):
    global fib_series

    print("fib(", n, ") = ", end=" ")
    bottom_up_fib(n)
    print()


    global count
    count_of_each_technique['bottom_up']=count

    print_series()


def bottom_up_fib(n):

    global  fib_series
    if n==0:
        return 0
    if n==1:
        return  1
    fib_series[0]=0
    fib_series[1]=1
    counter()
    counter()

    for i in range(2,n+1):
        fib_series[i]=fib_series[i-1]+fib_series[i-2]
        counter()
        print("fib({0})".format(i), end=" + ")

    return  fib_series[n]


while True:

    n = int(input("please enter n <-1 to exit>- "))
    if n==-1:
        break

    print("normal recursion : ")
    normal_recursion(n)
    print("\ntop down : ")
    top_down(n)
    print("\nbottom up : ")
    bottom_up(n)

    print("\nn = ",n)
    for k,v in count_of_each_technique.items():
        print(k," : ",v)



