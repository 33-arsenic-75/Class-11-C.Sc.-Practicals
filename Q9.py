def Fi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fi(n-1)+Fi(n-2)

def program():
    q=int(input("Enter a number here: "))
    for i in range(0,q):
        print(Fi(i+1))
program()
