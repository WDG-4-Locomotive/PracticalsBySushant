# Write a Python Program to print Fibonacci series up to the entered n positive number.

terms = int(input("Enter the nth term \n"))#AWESOME SUSHANT
nth = 0
n1, n2 = 0, 1
if terms < 0 or terms == 0 :
    while terms <= 0:
        terms = int(input("Enter number greater than 0 \n"))#AWESOME SUSHANT

elif terms == 1 :
    print(f"Fibonacci series for the given {terms} is {n2} ")

elif terms > 1:
    print(f"Fibonacci series for {terms} is ")
    while nth < terms :
        print(n1,end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth

# Output
# Enter the nth term 
# 99999
# Fibonacci series for 99999 is 
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368
        
