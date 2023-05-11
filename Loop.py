"""stateName="Virginia"
for letter in stateName:
    print(letter,end='')"""
##########################
total=0.0
count=0
inputStr= int(input("Enter value:"))
for value in range(inputStr+1):
    if (inputStr !=""):
        value= float(inputStr)
        total=total + value
        count= count + 1
        inputStr=input("Enter value:")
        
if(count >0):
    average= total/count
    print(average)
else:
    average=0.0

###############################
for i in range(3):
    for j in range(4):
        print("[]", end='')
    print()
