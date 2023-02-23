def print_even_numbers(numbers_list):
    even_numbers = []
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)

n=int(input('enter the value: '))
numbers_list = []
for x in range(1,n+1):
    numbers_list.append(int(input('enter the value: ')))
print(numbers_list)
print_even_numbers(numbers_list)
