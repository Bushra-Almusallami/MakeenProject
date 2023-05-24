from functools import reduce

list1=[2,3,4,5]
result=reduce(lambda x,y:x+y**2,list1,0)
print(result)

