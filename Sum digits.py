"""x,y=input("enter 2 numbers:").split(' ')
print(x,y)"""
#########################################
n=input("enter numbers to sum:")
def sum_digits(n):
    sum1=0
    for i in n:
        sum1=sum1+int(i)
        
    return sum1
print(sum_digits(n))
