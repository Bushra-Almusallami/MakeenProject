string=input("Enter string to count the vowels:")

def CountVowels(string):
    count=0
    for char in string:
        if (char in "AaOoUuIiEe"):
            count=count+1
    return count

count= CountVowels(string)
print(count) 
