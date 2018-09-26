


def fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return  res

def euler(n):
    res=1
    for i in range(1,n+1):
        res=res+(1/fact(i))
    return  res


while True:
    n=int(input("enter n :<-1 to break> :  "))
    if n==-1:
        break
    sum=euler(n)
    print(sum)