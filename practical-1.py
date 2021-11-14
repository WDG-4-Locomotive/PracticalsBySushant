# Write a python program to Input three numbers and display the largest / smallest number.

first = float(input("Enter first no. \n"))#AWESOME SUSHANT
second = float(input("Enter second no. \n"))#AWESOME SUSHANT
third = float(input("Enter third no. \n"))#AWESOME SUSHANT

min_or_max = input("Do you want to find no. with maximum[max] value or number with minimum[min] value or both[max-min] maximum value and minimum value ?   \n")
min_or_max_without_error = min_or_max.upper()

def max_number() :  # creating function to determine number with max value
    if first >=second and first >=third:
        print(f'{first} is the number with maximum value')#AWESOME SUSHANT
    elif second >=first and second >=third:
        print(f'{second} is the number with maximum value')#AWESOME SUSHANT
    else:
        print(f'{third} is the number with maximum value')#AWESOME SUSHANT

def min_number() :  # creating function to determine number with min value
    if first <=second and first <=third:
        print(f'{first} is the number with minimum value')#AWESOME SUSHANT
    elif second <=first and second <=third:
        print(f'{second} is the number with minimum value')#AWESOME SUSHANT
    else:
        print(f'{third} is the number with minimum value')#AWESOME SUSHANT


if min_or_max_without_error == "MAX":
    max_number()
    print("Have a great day")
elif min_or_max_without_error == "MIN":
    min_number()
    print("Have a great day")
else:
    max_number()
    min_number()
    print("Have a great day")
    
#  Output 
#  Enter first no. 
#  625
#  Enter second no. 
#  2476
#  Enter third no. 
#  345
#  Do you want to find no. with maximun[max] value or number with minimum[min] value or both[max-min] maximum value and minimum value ?   
#  max-min
#  2476.0 is the number with maximun value
#  345.0 is the number with minimum value
#  Have a great day
