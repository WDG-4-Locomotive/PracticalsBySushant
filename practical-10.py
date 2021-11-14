# Write a Python Program to Count and display the number of vowels, consonants, uppercase, lowercase characters in string.

string = input("Enter any string \n")#AWESOME SUSHANT
vowels  = "aeiouAEIOU"
vowel_in_string = consonents_in_string = lowercase_in_string = uppercase_in_string = 0
#AWESOME SUSHANT
for i in string:
    if i in vowels:
        vowel_in_string += 1
    if i not in vowels:
        consonents_in_string += 1
    if i.islower():
        lowercase_in_string += 1
    if i.isupper():
        uppercase_in_string += 1
#AWESOME SUSHANT
print(f"""
In the given string 
vowels = {vowel_in_string}
consonants = {consonents_in_string}
lowercase letters = {lowercase_in_string}
uppercase letters = {uppercase_in_string}
""")

# Output
# Enter any string
# Awesome Sushant

# In the given string   
# vowels = 6
# consonants = 9        
# lowercase letters = 12
# uppercase letters = 2 
