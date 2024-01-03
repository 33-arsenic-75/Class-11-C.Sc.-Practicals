s=input("Enter a word here:")
alt=""
for i in range(len(s)):
    if i%2==0:
        alt+=s[i]
    else:
        alt+=s[i].upper()
print(alt)
