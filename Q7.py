n=int(input("Enter a number here:"))
m=n
Sum=0
x=len(str(n))

def Armstrong(a,b,c):
    for i in range(x):
        r=b%10
        b//=10
        c+=r**x

    if c==a:
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")

Armstrong(n,m,Sum)
