#  Write a Python program to replace the last element in a list with another list

def replace(list1,list2):
    list1[-1]= list2
    return list1

list1 = [1,2,3]
list2 = [4,5]
output = replace(list1,list2)
print(output)