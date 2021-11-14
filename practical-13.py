# Write a python program to input radius of circle and print its area and Circumference

radius = float(input("Enter radius of circle in cm \n"))
pi = 22/7

area = pi * radius**2
peri = 2 * pi * radius

print(f"Area of circle of radius {radius}cm = {area}cm sq.")
print(f"Circumference of circle of radius {radius}cm = {peri}cm")

#  Output 
# Enter radius of circle in cm 
# 467234
# Area of circle of radius 467234.0cm = 686109633804.5714cm sq.      
# Circumference of circle of radius 467234.0cm = 2936899.4285714286cm
