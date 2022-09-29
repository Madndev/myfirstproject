#to write 2 diff files and merge to single file
import os
fh1=open("developing_language.txt","w")
print("enter the number of language u need ")
n=int(input())
i=0
while(i<n):
    a=input("enter the dev lang")
    fh1.write(a+"\n")
    i=i+1
fh1.close()

fh2=open("web.txt","w")
print("enter the number of language u need ")
n=int(input())
i=0
while(i<n):
    a=input("enter the web lang")
    fh2.write(a+"\n")
    i=i+1
fh2.close()

fh1=open("developing_language.txt","r")
x1=fh1.read()

fh2=open("web.txt","r")
x2=fh2.read()

sc=open("mergerd.txt","w")
sc.write(x1+x2)





 
   
