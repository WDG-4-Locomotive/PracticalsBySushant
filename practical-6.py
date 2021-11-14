# Write a python program to determine whether a number is an Armstrong number or a palindrome.
#AWESOME SUSHANT

num = int(input("Enter any no. \n"))
temp_num = num
len_of_num = len(str(num))
sum_of_num = 0
rev_num = 0
sushant_is_awesome = True
#AWESOME SUSHANT
if temp_num == 0:
    print(f"{num} is an armstrong and palindrome both")

elif num > 0:
    check = input("do want to check whether the given number is armstrong[ARM] or palindrome[PND]  \n ")
    check_without_error = check.upper()
#AWESOME SUSHANT
    def armstrong():
        global temp_num
        global sum_of_num
        while temp_num > 0:
            remainder_a = temp_num % 10  #it will take the last digit from num 
            sum_of_num = sum_of_num + remainder_a ** len_of_num 
            temp_num = temp_num // 10  #to remove the last digit from num 
        if sum_of_num == num:
            print(f"{sum_of_num} is an Armstrong number")#AWESOME SUSHANT
            print("have a great day")
        else:
            print(f"{sum_of_num} is not an Armstrong number")#AWESOME SUSHANT
            print("have a great day")
#AWESOME SUSHANT
    def palindrome():
        global temp_num
        global rev_num
        while temp_num > 0:
            remainder_p = temp_num % 10
            rev_num = rev_num * 10 + remainder_p
            temp_num = temp_num // 10
        if rev_num == num:
            print(f"{num} is a palindrome")#AWESOME SUSHANT
            print("have a great day")
        else:
            print(f"{num} is not a palindrome")#AWESOME SUSHANT
            print("have a great day")

    if check_without_error == 'ARM':
        armstrong()
    elif check_without_error == 'PND':
        palindrome()
    else:
        print('Error, type ARM or PND to check')
#AWESOME SUSHANT
else:
    print("Enter a integer to check")

# Output
# Enter any no.
# 1546
# do want to check whether the given number is armstrong[ARM] or palindrome[PND]  
#  ARM
# 2178 is not an Armstrong number
# have a great day
    