import math
n=int(input("enter the number of sides:"))
side=float(input("enter the side:"))

def area(n,side):
    area=(n*side**2)/(4*math.tan(3.14/n))
    return area

print("The area of the polygon is ",area(n,side))
