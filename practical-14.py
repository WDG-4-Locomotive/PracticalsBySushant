# Write a program to input principal ,rate and time from user and print simple interest.
prin_amount = float(input("Enter priciple amount in ₹ \n"))
rate = float(input("Enter rate of interest \n"))
time = float(input("Enter time in years \n"))
SI = prin_amount * rate * time / 100

print(f"Simple Intrest = {SI}₹")

#  Output 
#  Enter priciple amount in ₹
#  345435
#  Enter rate of interest 
#  345
#  Enter time in years 
#  3 
#  Simple Intrest = 3575252.25₹