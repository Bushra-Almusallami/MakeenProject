x=['1','2','3','4','5']

for i in x:
    s="|".join(x)
print(s)

######################
result=[]
for i in range(5):
    if(i%2==0):
        result.append(i)
print(result)
###########################another solution

"""result=[]
result=[i for i in range(5) if i%2==0]
print(result)"""

#########################


