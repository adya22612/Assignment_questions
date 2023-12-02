n=int(input())

# Variable count is initialised to zero
count=0

""" If the given constraints are satisfied 
    use a nested loop to determine the count of numbers containing digit 1  
    by converting the numbers to string and adding 1 everytime string 1 is found"""
if 0 <= n <= 109:
    for i in range(0,n+1):
        for j in str(i):
            if j =='1':
                count+=1
# The count value after satisfying the conditions
print(count)