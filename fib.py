def fib(n):
    list = [0, 1]
    if n <= 0:
        print("Enter a positive integer.")
    elif n == 1:
        print(list[0])
    elif n == 2:
        print(*list)
    else:
        for i in range(2, n):
            list.append(list[i-1] + list[i-2])
        print(*list)

n = int(input("Enter the number of terms: "))
fib(n)
