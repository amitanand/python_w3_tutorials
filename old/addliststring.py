import time

list_1=[]
i=0
n=int(input("Enter the no of items you want to insert in the list : "))
while i <n:
    element=input("Enter the element of the list :")
    list_1.append(element)
    i+=1
time.sleep(1)
print("Appending items in the list ...")
time.sleep(1)
print("List : ",list_1)

string_1="Appending lists"

string_2=str(list_1)
time.sleep(1)
print("Appending string and lists ...")
final_string=string_1+string_2
time.sleep(1)
print("Final_Result :",final_string)



