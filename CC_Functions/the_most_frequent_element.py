'''
Given a list, return the most frequent (repeating) element.
Note : If there are the same number of repeating elements, 
it returns the first element that repeats most from left to right in the list.
'''

def most_freq(given_list):
    return max(given_list, key = given_list.count)

print(most_freq([1,2,3,3,3,3,4,4,5,5])) 
#3
print(most_freq([1,1,2,3,3])) 
#1
print(most_freq([3,1,2,1,3])) 
#3
