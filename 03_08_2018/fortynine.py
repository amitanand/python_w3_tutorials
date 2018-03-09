# Write a Python program to convert list to list of dictionaries.

def listToDict(list1,list2):
    if len(list1) == len(list2):
        final_dict = {}
        for i in range(len(list1)):
            final_dict[list1[i]] = list2[i]
    else:
         print("ERROR ! Length are different. Mapping can't be done.")


    return final_dict

list1 = [1,2,3,4]
list2 = ['a','b','c','d']
output = listToDict(list1,list2)
print(output)