#simple move
import os
import shutil
src=r"C:\Users\appub\OneDrive\Desktop\py_folder\copy3.txt"
dst=r"C:\Users\appub\OneDrive\Desktop\py_folder\files.docx"
shutil.move(src,dst)


#copy file by checking if already there and then change the name and copy
import os
import shutil
src=r"C:\Users\appub\OneDrive\Desktop\py_folder"
dst=r"C:\Users\appub\OneDrive\Desktop\py_folder\files.docx"
file_name="copy_1.docx"
file_path=os.path.join(dst,file_name)
print(file_path)
if(os.path.isfile(file_path)):
    data=os.path.splitext(file_name)
    only_name=data[0]
    ext=data[1]
    new_base=only_name+"_new"+ext
    print(new_base)
    new_name=os.path.join(dst,new_base)
    print(new_name)
    shutil.move(src+"\\"+file_name,new_name)
else:
    shutil.move(src+"\\"+file_name,dst+"\\"+file_name)


 #check all the folders for particular file and copy them to a new destination folder which is empty
import os
import shutil
import glob
word_file=[]
src=r"C:\Users\appub\OneDrive\Desktop\py_folder"
dst=r"C:\Users\appub\OneDrive\Desktop\py_folder\files.docx"
pattern="**\**\*.txt"
fn=src+patternṇṇ
files=glob.glob(fn,recursive=True)
for file_name in files:
      shutil.copy(file_name,dst)
