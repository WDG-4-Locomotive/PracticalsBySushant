# Print following pattern
# A
# ABC
# ABCD
# ABCDE

rows = int(input("Enter No. of rows   \n"))#AWESOME SUSHANT
letter = 65
for i in range(1,rows+1):
    for j in range(letter,i+letter):
        print(chr(j),end="")
    print(' ')

# Output 
# Enter No. of rows   
# 5
# A 
# AB
# ABC
# ABCD
# ABCDE