#  Write a Python program to compute the similarity between two lists.

def similarity(list1,list2):
    present_There = []
    not_There = []
    if len(list1)>len(list2):
        for i in range(len(list2)):
            if list2[i] in list1:
                present_There.append(list2[i])
            else:
                not_There.append(list2[i])
    else:
        for i in range(len(list1)):
            if list1[i] in list2:
                present_There.append(list1[i])
            else:
                not_There.append(list1[i])


    return present_There,not_There






list2 = ["red", "orange", "green", "blue", "white"]
list1 = ["black", "yellow", "green", "blue"]
o1,o2 = similarity(list1,list2)
print(o1,o2)