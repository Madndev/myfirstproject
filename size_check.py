#to check the size

import os
def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

f_size = os.path.getsize(r"C:\Users\appub\OneDrive\Desktop\MAGZINE\E3.jpg")
x = convert_bytes(f_size)
print('file size is', x)
