wordList=[]
charDict = {}
new_word = input("Enter a string: ")
while new_word.lower()!="exit":
   wordList.append(new_word)
   new_word = input("Enter a string: ")

for word in wordList:
    for char in word:
        if char in charDict: 
            charDict[char]+= 1
        else: 
            charDict[char] = 1 

keyList = list(charDict.keys())
valueList = list(charDict.values())

max = 0
for i in valueList:
    if i > max:
        max = i
    
print(keyList[valueList.index(max)] + ' -> ' + str(max))


