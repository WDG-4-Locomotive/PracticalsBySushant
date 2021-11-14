# Write a python program to input the value of x and n and print the output of the series  x + x^2/2 + x^3/3 + x^4/4 - ........... x^n/n

no_for_exponent = float(input("Enter any number for exponent  \n "))#AWESOME SUSHANT
exponent_power = int(input("Enter any number for exponent power (no. should be ineger)  \n "))#AWESOME SUSHANT
sum_of_series = 0

for a in range(1,exponent_power+1):
    sum_of_series = sum_of_series + (no_for_exponent**a)/a

print(f"Sum of the series \"x + x^2/2 + x^3/3 + x^4/4 - ...... x^n/n\" for \"x\" = {no_for_exponent} and \"n\" = {exponent_power} is {sum_of_series}")

# Output
# Enter any number for exponent
# 342
# Enter any number for exponent power (no. should be ineger)  
# 4
# Sum of the series "x + x^2/2 + x^3/3 + x^4/4 - ...... x^n/n" for "x" = 342.0 and "n" = 4 is 3433537044.0
