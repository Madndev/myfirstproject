#search and replace
s=input("what do u want to replace")
r=input("by which word do u want to replace")
fh=open(r"C:\Users\appub\OneDrive\Desktop\py_folder\content.txt","r")
txt= fh.read()
txt=txt.replace(s,r)
fh.close()
fh=open(r"C:\Users\appub\OneDrive\Desktop\py_folder\content.txt","w")
fh.write(txt)
fh.close()



#search and remove
import os
s=input("what do u want to remove")
fh=open(r"C:\Users\appub\OneDrive\Desktop\py_folder\content.txt","r")
txt= fh.read()
txt=txt.replace(s,"")
fh.close()
fh=open(r"C:\Users\appub\OneDrive\Desktop\py_folder\content.txt","w")
fh.write(txt)
fh.close()
