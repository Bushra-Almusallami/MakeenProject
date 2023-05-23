#lst=["Said,25","Majid,19","Salim,32","Ali,21","Sultan,28"]
"""new1=[]
new2=[]

def Sort(lst):    
    for i in range(len(lst)):
        n=lst[i].split(",")
        new1.append(int(n[1]))
    print(new1)
    for i in range(len(lst)):
            n=lst[i].split(",")
            new2.append(str(n[0]))
    print(new2)"""
new2=[]

def InsertionSort(lst):
      
    for m in range(1,len(lst)):
        key=lst[m]
        j= m-1
        
        while j >= 0 and key.split(",")[1] < lst[j].split(",")[1]:
            lst[j+1]= lst[j]
            j=j - 1
            
        lst[j+1]=key
    print(lst)
    
lst=["Said,25","Majid,19","Salim,32","Ali,21","Sultan,28"]

InsertionSort(lst)

for i in range(len(lst)):
    n=lst[i].split(",")
    new2.append(str(n[0]))
print(new2)
