#Given two integer values, return their sum. 
#If the two values are the same, then return double their sum.

def sum_double(x, y):
    if x==y:
        return 2 * (x+y)
    else:
        return x+y

print(sum_double(1, 2))
#3
print(sum_double(5, 7))
#12
print(sum_double(5, 5))
#20
