'''
<< is the left-shift operator, and has the effect of multiplying the left hand side by two to the power of the right hand side:
x << n == x * 2**n
'''

def powerset(list1):
    size = len(list1)

    for i in range(1, 1 << size):
        print([list1[item] for item in range(size) if (i & (1 << item))])


list1 = ['a', 'b', 'c', 'd']

powerset(list1)
