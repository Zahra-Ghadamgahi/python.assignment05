def print_checkboard(m,n):
    for i in range(m):
        for j in range(n):
            if(i+j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    
print_checkboard(6, 7)
    