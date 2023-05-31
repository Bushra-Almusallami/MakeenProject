import math

#Humidity
entropyall=(-9/14)*math.log(9/14,2)-(5/14)*math.log(5/14,2)
yes=(-3/7)*math.log(3/7,2)-(4/7)*math.log(4/7,2)
no=(-6/7)*math.log(6/7,2)-(1/7)*math.log(1/7,2)

#knowledge gain of humidity
kg= 0.94-7/14*0.98-7/14*0.59

print(yes)
print(no) 
print(kg)
