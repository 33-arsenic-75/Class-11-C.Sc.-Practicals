p=float(input("Enter principal amount here:"))
r=float(input("Enter interest rate here:"))
t=float(input("Enter no. of years for which the money was borrowed:"))
si=p*r*t/100
ci=p*((1+(r/100))**t)-p
print("Simple interest=",si)
print("Compound interest=",ci)
