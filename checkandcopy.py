import os
fh = open("developer.txt","w")
n=int(input("how many developing languages do u want : "))
i=0
while(i<n):
    dev=input("enter the developing programas : ")
    fh.write(dev+"\n")
    i+=1  
fh.close()

fh1 = open("web.txt","w")
n=int(input("how many web languages do u want : "))
i=0
while(i<n):
    dev=input("enter the web programing languages : ")
    fh1.write(dev+"\n")
    i+=1
fh1.close()


fh = open("developer.txt","r")
d1 = fh.read()
fh1 = open("web.txt","r")
d2 = fh1.read()


sc=open("coes.txt","w")
sc.write(d1+d2)