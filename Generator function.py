def fun1(nums):
    x,y=0,1
    for i in range(nums):
        x,y=y,x+y
        yield x

def fun2(nums):
    for num in nums:
        yield num**2
        
def fun3(nums):
    for n in nums:
        yield n**3

print(sum(fun3(fun2(fun1(10)))))
