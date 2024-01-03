s=input("Enter a sentence here: ")
l=['a','e','i','o','u','A','E','I','O','U']
vc=0
for i in range(len(s)):
    if s[i] in l:
        vc+=1
print("No. of vowels =",vc)
