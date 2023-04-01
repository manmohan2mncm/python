n=int(input("enter the no of values in the list: "))

list=[]
for x in range(n):
    list.append(input("enter the value: "))
print(list)

for x in range(n):
    for y in range(n-1):
        if(list[y]>list[int(y+1)]):
            c=list[y]
            list[y]=list[int(y+1)]
            list[int(y+1)]=c

print('\n')
print(list)
