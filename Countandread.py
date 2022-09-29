import os
with open(r"C:\Users\Desktop\codes\merge.txt", 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if line.find("\n") != -1:
            print('Line Number:', lines.index(line))
            print('Line:', line)
