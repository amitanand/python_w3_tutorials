# Write a Python program to change the position of every n-th value with the (n+1)th in a list

def changePos(list1):
    for i in range(0,len(list1),2):
            list1[i],list1[i+1] = list1[i+1],list1[i]

    return list1

list1= [7,8,6,5,4,2]
output = changePos(list1)
print(output)