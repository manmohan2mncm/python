def sum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    return sum

n = int(input("Enter a number: "))
print(sum(n))
