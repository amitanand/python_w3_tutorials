import time

x=int(input("Please enter the first number :"))
y=int(input("Please enter the second number :"))
i=1
factorsof_x=set()
factorsof_y=set()
for i in range(1,x+1):
    if x%i==0:
        factorsof_x.add(i)
print("Calculating factors of",x,"...")
time.sleep(1)
print(factorsof_x)

for i in range(1,y+1):
    if y%i==0:
        factorsof_y.add(i)
print("Calculating factors of",y,"...")
time.sleep(1)
print(factorsof_y)
time.sleep(1)
common_fact=factorsof_x.intersection(factorsof_y)
print("Calculating common factors ... ")
time.sleep(1)
print(common_fact)
time.sleep(1)
common_list=list(common_fact)
print("Calculating GCD of",x,"and",y,"...")
time.sleep(1)
print(max(common_list))


