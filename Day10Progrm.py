input1= open("readfile.txt","r")
employee={}
salary=[]
for line in input1:
    data= line.split()#list
    print(data)
    employee[data[1]]= data[0]
    salary.append(float(data[0]))
print(employee)     
print(salary)

avg= sum(salary)/len(salary)
print(avg)
x=max(salary)
print(x)
for i in employee:
    if(float(employee[i])== x):
        print(i,"has the maximun salary.")

