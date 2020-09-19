def isVowel(char1, char2):
    vowels='aeiou'
    if (char1 in vowels) and (char2 in vowels):
        return True
    else:
        return False

word=input("Please enter a word: ").lower()
def isConsecutive(word):
    vCounter=1
    if len(word)>1:           
        for i in range(0,len(word)-1):
            if isVowel(word[i], word[i+1]):
                vCounter+=1   
        if vCounter >= 2: 
            print("Positive!")
        else:
            print("Negative!")
    else:
        print("Warning! Please enter a word which is contains more than 2 chars.")

isConsecutive(word)
