import numpy as np
from numpy.random import randn
A= np.array([1,2,3,4])
B= np.array([100,200,300,400])
arr= randn(5,5)
arr
m=0
sd=1
arr= randn(5,5)+m*sd
arr
A=np.array([-2,5,4,-8,0])
print(np.sort(A)) #Ascending
print(np.sort(A)[::-1]) #Descending
names= np.array(['Bushra','Sara','Asma','Juhaina'])
np.unique(names)
np.in1d(['Sara','US','Asma'],names)  #check if there
