st=input("Enter a sentence here : ")
wl=st.split()
for i in wl:
    print("Word:", i+",", "Length=",len(i))
