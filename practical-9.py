# Write a Python Program to Compute the greatest common divisor(GCD/HCF) and least common multiple (LCM) of two Integers.

num1 = int(input("Enter first number \n"))#AWESOME SUSHANT
num2 = int(input("Enter second number \n"))#AWESOME SUSHANT

if num1 < num2 :
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

lcm = (num1 * num2) / hcf

print(f"HCF of {num1} and {num2} is {hcf} ")
print(f"LCM of {num1} and {num2} is {lcm} ")

# Output
# Enter first number 
# 25654646
# Enter second number 
# 546
# HCF of 25654646 and 546 is 2 
# LCM of 25654646 and 546 is 7003718358.0
