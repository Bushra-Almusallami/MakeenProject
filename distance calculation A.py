file= open("distance.txt","r")
d=0
for line in file:
    data= line.split()
    print(data)
    d=int(data[0])*int(data[1])
    print("the distance is",d)
