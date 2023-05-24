"""sum1= lambda x,y: x+y+1
print(sum1(3,4))

sum2= lambda x=1,y=3: (x+y)*2
print(sum2(3)) # x will be 3

sum3= lambda x=1,y=3: (x+y)*2 #x value will be take by default
print(sum3(y=5))"""

################################

people=[{'name':'Joun','Age':28},
        {'name':'Mary','Age':23},
        {'name':'Bob','Age':35},
        {'name':'Alice','Age':32}]
print(sorted(people,key=lambda n:n['Age']))
#people.sort(key=lambda x:x['Age'])
#print(people)
