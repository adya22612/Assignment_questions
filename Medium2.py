import numpy as np

# Taking multiple integer numbers and assigning it to variable nums forming a list
arr=list(map(int,input().split()))

""" If the given constraints are satisfied
    then np.unique gives unique elements in a sorted manner
    after which m_elements gives values which have repetitions 
    greater than n//3 in the form of a numpy array """
if (1 <= len(arr) <= 5 * 104) and (-109 <= num <= 109 for num in arr):
    n=len(arr)
    constraint=n//3
    elements,count=np.unique(arr,return_counts=True)
    m_elements=elements[count>constraint]
    print(m_elements)