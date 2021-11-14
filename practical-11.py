# Write a Python Program to Input a string and determine whether it is a palindrome or not; convert the case of characters in a string.

string = input("Enter a word \n")

string_u = string.upper()
string_l = string.lower()

rev_of_string = string[::-1]

rev_of_string_u = rev_of_string.upper()
rev_of_string_l = rev_of_string.lower()

if rev_of_string == string:          #AWESOME SUSHANT
    print(f"{string} is a palindrome")      #AWESOME SUSHANT

elif  rev_of_string_u == string_u and rev_of_string_l == string_l:
    print(f"{string} is not a palindrome but {rev_of_string_u} and {rev_of_string_l} are palindrome")

else:                     
        print(f"{string} is not a palindrome")      #AWESOME SUSHANT

# Output
# Enter a word 
# RaceCar
# RaceCar is not a palindrome but RACECAR and racecar are palindrome