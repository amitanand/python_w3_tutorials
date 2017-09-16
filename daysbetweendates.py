import time

#date mentioned here in in YY/M/DD format

SampleDate_1= (2014, 7, 2)
SampleDate_2=(2014, 7, 11)

 #As year & month are same we will focus on date

date=SampleDate_2[2] - SampleDate_1[2]
print("Calculating no of days between",SampleDate_2,"and",SampleDate_1,"is ...")
time.sleep(2)
print(date,"days")
