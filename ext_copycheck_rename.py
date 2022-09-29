from fileinput import filename
import os
import shutil 
import glob
src=r"C:\Users\donys\Desktop\codes"
dest=r"C:\Users\donys\Desktop\codes\copy\copy1.0"
pattern="**\**\*.txt"
fn=src+pattern
fn1=dest+pattern
files=glob.glob(fn,recursive=True)
files1=glob.glob(fn1,recursive=True)
for i in files: 
    if i in files1:
        print("already exists, we are renaming it")
        break1=(os.path.split(i))   
        break2=(break1[-1])
        break3=(os.path.splitext(break2))
        name=break3[0]
        ext=break3[1]
        newname=name+"_new"+ext
        newfile=os.path.join(dest,newname)
        shutil.copy(i,newfile)
    else:
        shutil.copy(i,dest)