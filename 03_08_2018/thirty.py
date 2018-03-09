# Write a Python program to get the frequency of the elements in a list.

import collections

def frequencyItem(listprovided):
    ctr = collections.Counter(listprovided)
    return ctr

listprovided = [1,2,5,4,2,1,2,3,2,1,5,4,2,1]
output = frequencyItem(listprovided)
print(output)