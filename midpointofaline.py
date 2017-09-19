import time

x1=int(input("Please enter the x-xordinate of point 1 :"))
y1=int(input("Please enter the y-xordinate of point 1 :"))
x2=int(input("Please enter the x-xordinate of point 2 :"))
y2=int(input("Please enter the y-xordinate of point 2 :"))

print("Calculating mid-points ...")
point_x=(x2+x1)/2
point_y=(y2+y1)/2
time.sleep(1)

print("Mid-point is :",point_x,point_y)


