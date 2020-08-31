#Define a function named my_min to find the min of the inputted numbers.

def my_min(*numbers):
    return min(numbers)

print(my_min(5,6,7))
#5
print(my_min(3,8,-9,0,12,1.2))
#-9
print(my_min(-100))
#-100
