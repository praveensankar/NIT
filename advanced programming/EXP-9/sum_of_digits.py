
while True:
    n = int(input("please enter the digit  <-1 to break> : "))
    if n==-1:
        break
    res=0
    temp=n
    while temp!=0:
        res=res+temp%10
        temp=temp//10
    print("result is :",res)



