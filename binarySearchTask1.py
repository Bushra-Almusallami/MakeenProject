def binarySearch(list1,key):
    
    low=0
    high=len(list1)-1
    
    while (high >= low):
        mid=(low+high)//2
        
        if (key == list1[mid]):
            return mid
        elif(key > list1[mid]):
            low= mid + 1
        else:
            high=mid -1
    return -1

list1=[1,3,4,5,6,10]
print(binarySearch(list1,10))
