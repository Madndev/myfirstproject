#factors of even and odd numbers

num1=int(input("enter the starting number::"))
num2=int(input("enter the last number"))

es=os=0
for i in range(num1,num2+1):
    if(i%2==0):
        es=es+i
        print("even numbers are",i)
        print("the factors of ",i,"are")
        for j in range(1,i+1):
            if i%j==0:
                print(j)

for i in range(num1,num2+1):
    if (i%2!=0):
        os=os+i
        print("odd num are",i)
        print("the factorial of ",i)
        for j in range (1,i+1):
            if i%j==0:
                print(j)

print("***********************")
print("the sum os even num are",es)
print("the sum of odd num are ",os)
