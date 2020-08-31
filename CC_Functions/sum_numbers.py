#Define a function named my_sum to return the sum of all int type inputted numbers.

def my_sum(*numbers):
    return sum(numbers)

print(my_sum(9, 1, 3, 0, -1))
#12
print(my_sum(5, 7, 4))
#16
print(my_sum(10, -20, 30, 40))
#60
