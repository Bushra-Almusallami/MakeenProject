"""rows=int(input("number of rows:"))
columns= int(input("number of columns:"))

lst=[]
for i in range(rows):
    rowInput=list(map(int, input("Enter elements of rows:"). strip(). split()))
    lst.append(rowInput)
print(lst)"""

##################################################

"""lst3=[]
for i in range(4):
    lst1=[]
    for j in range(4):
        if([i] >[j]):
            lst1.append(2)
        if([i] ==[j]):
            lst1.append(1)
        if([i] <[j]):
            lst1.append(0)
    lst3.append(lst1)
    
    
for i in range(4):
    for j in range(4):
        print(lst3[i][j], end=" ")
    print()"""
########################################
a=0
lst3=[]
for i in range(4):
    lst1=[]
    for j in range(4):
        a=i+j
        if(a%2==0):
            lst1.append(1)
        if(a%2!=0):
            lst1.append(0)

    lst3.append(lst1)
    print(lst3[i][j], end=" ")
print()
    
    
for i in range(4):
    for j in range(4):
        print(lst3[i][j], end=" ")
    print()
