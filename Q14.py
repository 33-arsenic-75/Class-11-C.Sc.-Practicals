st=input("Enter a sentence here : ")
wl=st.split()
lw=wl[0]
maxlen=len(lw)
for i in wl:
    if len(i)>maxlen:
        maxlen=len(i)
        lw=i
print("Longest word:",lw)
print("Length=",maxlen)
