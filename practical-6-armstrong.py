# Write a python program to determine whether a number is an Armstrong number or not.

num = int(input("Enter any number to check whether it is Armstrong or not \n"))
num_length = len(str(num))
num_sum = 0
ori_num = num

while num > 0:
    remainder = num % 10
    num_sum = num_sum + remainder ** num_length
    num //=10

if num_sum == ori_num:
    print(f"{num_sum} is an Armstrong ")
        
else:
    print(f"{ori_num} is not an Armstrong")

# Output
# Enter any number to check whether it is Armstrong or not 
# 370
# 370 is an Armstrong 