import os
import shutil
import glob
src=r"C:\Users\appub\OneDrive\Desktop\py_folder"
dest=r"C:\Users\appub\OneDrive\Desktop\py_folder\files.docx"
pattern="**\**\*.py"
fn=src+pattern
fn1=dest+pattern
files=glob.glob(fn,recursive=True)
for file_name in files:
    if file_name==dest:
        new_name=
    shutil.copy(file_name,dest)
    
