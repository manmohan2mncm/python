a=int(input("enter the value: "))
i=0
for x in range(1,a+1):
    if(x%a==0):
        i=i+1
if(i==2):
    print(a,"is prime")
else:
    print(a,"is not prime")
