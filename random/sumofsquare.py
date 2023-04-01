def sum_of_squares(numbers):
    sum = 0
    for num in numbers:
        sum += num**2
    return sum

numbers = [1, 2, 3, 4, 5]
print(sum_of_squares(numbers))
