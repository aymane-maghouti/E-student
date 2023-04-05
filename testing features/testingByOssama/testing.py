
f=open("hi.txt","w").close()
with open("hi.txt","r+") as f:
    f.write("sssssss")
    c=f.read()
    print(c)
    f.seek(len(c))
    f.write("end")
