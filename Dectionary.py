#Find which person age is >22

Dectionary={1:{"Name":"P1",
               "Age":22},
            2:{"Name":"P2",
               "Age":27}}
for key in Dectionary:
    if Dectionary[key]["Age"] > 22:
        print(Dectionary[key]["Name"])
        
###################### Another solution
for key in Dectionary:
    x=Dectionary[key]["Age"]
    if x > 22:
        print(Dectionary[key]["Name"])
