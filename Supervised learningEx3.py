#Create a list of 10 random integers between 1 and 100.
# Standardize the numbers
# Normalize the numbers


from sklearn.preprocessing import StandardScaler
import numpy as np

data= np.random.randint(1,101, size=(10,1))
print("Origenal numbers:\n",data)

#standarize numbers
scaler= StandardScaler()
scaler.fit(data)
standarized_data= scaler.transform(data)
print("standarize numbers\n",standarized_data)

#normalize numbers
min_lst=min(data)
max_lst=max(data)

for i, val in enumerate(data):
    data[i] = (val-min_lst) / (max_lst-min_lst)
print("normalize numbers:\n",data)
