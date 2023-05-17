"""list1=[[1,2,3],
       [4,5,6]]

for i in list1:
    print(i[0],end=" ")"""
    
#############################
"""list1=[[1,2,3],
       [4,5,6]]

for i in range(2):  ##rows
    for j in range(3):
        print(list1[i][j],end=" ")
    print()"""

##############################

"""b= [[0]*3 for i in range(3)]
print(b, end=" ")"""
################################
lst=[[i+1]*3 for i in range(3)]
#print(lst)
for i in range(3):
    for j in range(3):
        print(lst[i][j], end=" ")
    print()