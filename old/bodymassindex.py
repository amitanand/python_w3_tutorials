import time

weight = float(input("Please enter your weight (in pounds) :"))
height = float(input("Please input your height (in inches) :"))
print("Calculating your BMI ...")
weight_kg = weight/2.2
height_metres=height/39.37
bmi=weight_kg/height_metres
time.sleep(1)
print("Your BMI :",bmi)