
length=input("Enter word:")
x=len(length)


mid=x//2
#if number is 1.5 it will be 1


if(x%2 == 0):
    print(length[mid-1],length[mid])
else:
    print(length[mid])