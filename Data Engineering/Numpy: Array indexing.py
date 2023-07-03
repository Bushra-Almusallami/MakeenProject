import numpy as np
arr=np.arange(0,10)
arr
arr[2]     #3d element
arr[1:5]
arr1=np.array([[1,2,3,4],[21,23,25,33],[3,6,9,8],[4,12,9,10]])
arr1
arr1[1,0]   #row 2, column 1
arr1[:2,2:]     # first 2 rows, last 2 columns
arr[:3]   #first 3 elements
arr2=np.array([[1,2,3],[21,23,25],[3,6,9]])
arr2
arr2[:2,1:]      # first 2 rows, last 2 columns
arr2[:3,::2]    #first 3 rows, first and second columns
reshape1 = np.arange(0,9).reshape(3,3)
reshape1
arr2.reshape(-1)   #2D to 1D
