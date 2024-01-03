n=int(input("Enter a number to generate its pattern:"))
for i in range(1,n):
    for j in range(i):
        print("*", end=" ")
    print()
for k in range(n,0,-1):
    for l in range(k):
        print("*", end=" ")
    print()
