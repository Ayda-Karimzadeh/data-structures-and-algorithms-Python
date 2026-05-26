def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)

# n^2 is the dominant term and that stand alone n is the non-dominant term
# big O = O(n^2) + O(n)
# big O = O(n^2) we drop O(n)