def even(nums):
    for num in range(15):
        if num%2==0:
            yield num
            
value=even(15)
for i in value:
    print(i)
