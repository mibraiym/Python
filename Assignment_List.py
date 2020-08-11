''' Task : Find out the most frequent number and its frequency.
Write a program that; 
	Finds out the most frequent number in the given list.
	Calculates its frequency.
	Prints out the result such as : "the most frequent number is {number} and it was {count} times repeated" '''

''' Option_1 Using for loop to count the frequency of each element. 
If the current frequency (frequency) is greater than the previous frequency (temp_frequency),
update the counter (count) and store the element.'''

def most_frequent(List): 
	frequency = 0
	item = List[0] 
	
	for i in List: 
		temp_frequency = List.count(i) 
		if(temp_frequency> frequency): 
			frequency = temp_frequency 
			item = i 

	return f"The most frequent number is {item} and it was {frequency} times repeated."

List = [2, 1, 2, 2, 1, 3] 
print(most_frequent(List)) 

''' Option_2 Using python dictionary to save element as a key and its frequency as 
the value, and thus find the most frequent element.'''

''' def most_frequent(List): 
	dict = {} 
	item, frequency = '', 0 
	for i in List: 
		dict[i] = dict.get(i, 0) + 1
		if dict[i] >= frequency : 
			item, frequency = i, dict[i] 
	return f"The most frequent number is {item} and it was {frequency} times repeated."

List = [2, 1, 2, 2, 1, 3, 3 ,3 ,3] 
print(most_frequent(List)) '''

''' Option_3 Make a set of the list so that the duplicate elements are deleted. 
Then find the highest count of occurrences of each element in the set and thus, 
we find the maximum out of it. '''

''' def most_frequent(List): 
	return f"The most frequent number is {max(set(List), key = List.count)} and it was {List.count(max(set(List), key = List.count))} times repeated." 

List = [2, 1, 2, 2, 1, 3] 
print(most_frequent(List)) '''