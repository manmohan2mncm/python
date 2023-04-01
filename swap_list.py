my=['1','2','4','9','67','44']

h=int(input('enter the index: '))
i=int(input('enter the index: '))

c=my[h]
my[h]=my[i]
my[i]=c

print(my)
