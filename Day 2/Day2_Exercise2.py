# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_int = int(weight)
height_float = float(height)

bmi = weight_int / (height_float * height_float)
bmi_int = int(bmi)
print(bmi_int)
