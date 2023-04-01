def sum(y):
    sum = 0
    while y > 0:
        digit = y % 10
        sum = sum + digit
        y = y // 10
    return sum

my=[25,45,56767,34,12,10]
l=len(my)
for x in range(l):
    y=my[x]
    my[x]=sum(y)

print(my)
