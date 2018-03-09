# Write a Python program to check if all items of a list is equal to a given string

def equalList(list1,list2,string1):
    print(string1)
    i = 0
    while i <len(list1):
        if string1 != list1[i]:
            print("NOT EQUAL IN LIST1")
            break
            i += 1


        else:
            print("EQUAl IN LIST1")
            break


    for j in range(len(list2)):
        if string1 != list2[i]:
            print("NOT EQUAL IN LIST2")
            break
            i += 1

        else:
            print("EQUAL IN LIST1")
            break


list1 = ["green", "orange", "black", "white"]
list2 = ["green", "green", "green", "green"]
string1 = str(input("Please enter the item :"))
equalList(list1,list2,string1)