def multiply_numbers(numbers_list):
    result = 1
    for num in numbers_list:
        result *= num
    return result


numbers_list = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers_list)
print("multiplication of all numbers in the list: ",result)
