#Create a list of 1000 random integers between 1 and 100000, then calculate the Z-Score
#to check for the outliers. Consider values Z-Score > 2 as outliers 

import random
import numpy as np 
 
random_lst=[]
n=1000
for i in range(n):
    random_lst.append(random.randint(1,100000))
print(random_lst)

mean = np.mean(random_lst)
std = np.std(random_lst)
print('mean is: ', mean)
print('std is: ', std)

outlier = []
for i in random_lst:
    z = (i-mean)/std
    print(z)
    if z > 2:
        outlier.append(i)
print('outlier is: ', outlier)
