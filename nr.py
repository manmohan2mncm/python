import math

def fact(n,r):
    a=math.factorial(n)
    b=math.factorial(n-r)
    c=math.factorial(r)
    print((a/b)*c)

n=int(input("enter the value: "))
r= int(input("enter the value: "))

fact(n,r)
