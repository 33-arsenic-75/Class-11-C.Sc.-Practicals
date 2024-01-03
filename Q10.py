n=int(input("Enter a number to generate pattern:"))
for i in range(n):
    for j in range(n-i):
        print(n-j,end=' ')
    print()
    
