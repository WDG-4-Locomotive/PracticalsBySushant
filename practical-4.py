# Print following pattern
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

rows = int(input("Enter No. of rows   \n"))#AWESOME SUSHANT
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j,end="")
    print(' ')

# Output
# Enter No. of rows   
# 5
# 12345
# 1234
# 123
# 12
# 1

