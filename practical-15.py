# Write a python program to Input your name and display welcome message.
name = input("Enter your name \n")

import datetime
time = datetime.datetime.now()

if (time.hour > 18) :
    greeting = 'Good evening!'
elif (time.hour > 12) :
    greeting = 'Good afternoon!'
elif (time.hour > 0) :
    greeting = 'Good morning!'
else :
    greeting = 'Welcome!'
# Awesome Sushant
print(f"{greeting} {name}")

#  Output
#  Enter your name
#  Sushant
#  Good morning! Sushant
