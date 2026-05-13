def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

# when we printed this on the screen, we got
# n times n times printing out. 
# n * n = n^2 -> O(n^2)