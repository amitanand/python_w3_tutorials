import time

n=int(input("Enter the number to which you want to find the sum : "))
list_1=[]
i=0
for i in range(n+1):
    list_1.append(i)
    i+=1

print("Adding all the integers till",n)
time.sleep(1)
print("Sum :",sum(list_1))
