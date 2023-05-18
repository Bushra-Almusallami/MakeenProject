file= open("factors.txt","r")
f=[]
c=0
for line in file:
    n= line.split()
    print(n)
    i=0
    while c<=10:
        if(counter%2==0):
            i=i+1
            print(counter)
            counter=counter+2

