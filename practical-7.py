# Write a python program to Input a number and check if the number is a prime or composite number.

num = int(input("Enter any number to check whether the no. is prime or composite  \n"))#AWESOME SUSHANT

if num == 0 or num == 1:
    print("Zero(0) and One(1) are neither prime nor composite, enter no. above 1 to check.")#AWESOME SUSHANT
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is a Composite number")#AWESOME SUSHANT
            break
        else:
            print(f"{num} is a prime number")#AWESOME SUSHANT
            break
else:
    print("ERROR, Enter a integer to check")#AWESOME SUSHANT

# Output
# Enter any number to check whether the no. is prime or composite  
# 127
# 127 is a prime number
