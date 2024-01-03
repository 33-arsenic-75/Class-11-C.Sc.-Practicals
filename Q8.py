print("This program will calculate the sum of the series [1 + (1+2) + (1+2+3) + ... + (1+2+3+...+n)]")
n=int(input("Enter the value of n here : "))
Sum=0
for i in range (0,n+1):
    Sum+=i*(i+1)/2
print("The sum of the series is",Sum)
