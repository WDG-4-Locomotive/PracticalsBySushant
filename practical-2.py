# Write a python program to input the value of x and n and print the output of the series 1 - x^1 + x^2 - x^3 + x^4 - ......... x^n

no_for_exponent = float(input("Enter any number for exponent   \n"))#AWESOME SUSHANT
exponent_power = int(input("Enter any number for exponent power (no. should be ineger)  \n "))#AWESOME SUSHANT
sum_of_series = 0

for s in range(exponent_power + 1):
    sum_of_series = sum_of_series + (no_for_exponent**s)
    no_for_exponent = no_for_exponent * -1

abs_no_for_exponent = abs(no_for_exponent)

print(f"Sum of the series \"1 - x^1 + x^2 - x^3 + x^4 - .... x^n\" for \"x\" = {abs_no_for_exponent} and \"n\" = {exponent_power} is {sum_of_series}")

# Output
# Enter any number for exponent   
# 525
# Enter any number for exponent power (no. should be ineger)  
#  5
# Sum of the series "1 - x^1 + x^2 - x^3 + x^4 - .... x^n" for "x" = 525.0 and "n" = 5 is -39807974115524.0