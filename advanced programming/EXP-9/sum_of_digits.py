
while True:
    n = int(input("please enter the digit  <-1 to break> : "))
    if n==-1:
        break
    res=0
    temp=n
    while temp!=0:
        res=res+temp%10
        temp=temp//10

    res1=0
    tmp=res
    while res!=0:
        res1=res1+res%10
        res=res//10
    print("result is :",tmp,res1)



