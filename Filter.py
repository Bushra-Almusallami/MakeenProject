def lower_case(lower):
    return lower.islower()

list1=["bushra","sara","BUSHRA"]
lower1=list(filter(lower_case,list1))
lower2=list(filter(lambda lower:lower.islower(),list1))
print(lower1)
print(lower2)


