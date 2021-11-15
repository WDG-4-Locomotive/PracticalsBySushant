# Write a python program to determine whether a number palindrome or not.

num = int(input("Enter any number to check whether it is Palindrome or not \n"))
num_sum = 0
ori_num = num

while num > 0:
    remainder = num % 10
    num_sum = num_sum * 10 + remainder
    num //=10

if num_sum == ori_num:
    print(f"{num_sum} is a palindrome ")
        
else:
    print(f"{ori_num} is not a palindrome")

# Output
# Enter any number to check whether it is Armstrong or not 
# 434
# 434 is a palindrome