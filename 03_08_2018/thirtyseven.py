# Write a Python program to find common items from two lists

def commoninList (list1,list2):
    commonEle = []
    if len(list1)<len(list2):
        for i in range(len(list1)):
            if list1[i] in list2:
                commonEle.append(list1[i])
            else:
                print('Nothing in common')
    else:
        for i in range(len(list2)):
            if list2[i] in list1:
                commonEle.append(list2[i])
            else:
                print("Nothing in common")

    return commonEle

list1 = [3,4,5,6,7,8]
list2 = [10]
output = commoninList(list1,list2)
print(output)
