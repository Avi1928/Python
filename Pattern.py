for row in range(1,6):
    for coloumn in range(1,row+1):
        print(coloumn,end=' ')
    print("\n")

print("---------------------------")

for row in range(5,0,-1):
    for coloumn in range(1,row+1):
        print(coloumn,end=" ")
    print("\n")

print("---------------------------")

for row in range(5,0,-1):
    for coloumn in range(row,6):
        print(row,end=" ")
    print("\n")
