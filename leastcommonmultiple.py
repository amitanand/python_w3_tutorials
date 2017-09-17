x=int(input("Please enter the first number :"))
y=int(input("Please enter the second number :"))
multiple_x=set()
multiple_y=set()
i=1
for i in range(1,100):
    number=i*x
    multiple_x.add(number)
    #print(number)
for i in range(1,100):
    number=i*y
    multiple_y.add(number)

common_nultiple=multiple_x.intersection(multiple_y)
list_common_multiple=list(common_nultiple)
print("LCM of",x,"and",y," is :",min(list_common_multiple))

