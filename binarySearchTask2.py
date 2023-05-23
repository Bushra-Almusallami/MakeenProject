def binarySearch(key):
    
        low=0
        high=key//2
        
        while (high >= low):
            mid=(low+high)//2
            
            if (key == mid*mid):
                return mid
            elif(key > mid*mid):
                low= mid + 1
            else:
                high=mid -1
        return -1

print(binarySearch(100))
