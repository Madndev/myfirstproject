file=(open(r"C:\Users\appub\OneDrive\Desktop\py_folder\hello.txt","r"))
re=file.read()
for i in reversed(re):
    print(i,end="")
