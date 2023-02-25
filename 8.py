s=int(input('enter the value to seacrh: '))

my=[1,2,4,9,67,44]

l=len(my)
for x in range(l):
    if(my[x]==s):
        print('found')
        break
    else:
        print('not found')
