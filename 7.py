a=int(input("enter the value of a: "))
sum=0
for x in range(1,a):
    if(a%x==0):
        sum=sum+x
if(sum==a):
    print("perfect number")
else:
    print("not a perfect number")
