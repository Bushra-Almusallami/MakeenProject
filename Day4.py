"""x=int(input("Enter memory:"))
n=int(input("Enter number of files:"))
y=int(input("Enter size of file:"))
Totalsize=y*n

if(Totalsize<x):
    print("yes")
else:
    print("No")"""
##################################
word='Hello'
print(ord(word[0]),ord(word[1]),ord(word[2]),ord(word[3]),ord(word[4]))
##another sulotion
str1 = input("Please Enter your Own String : ")
i = 0

while(i < len(str1)):
    print("The ASCII Value of Character %c = %d" %(str1[i], ord(str1[i])))
    i = i + 1
##################################
#find the factors of a number

"""n=int(input("Enter a number:"))

x=1
while x<=n:
    if(n%x==0):
        print(x)
    x=x+1"""