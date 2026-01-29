#wap to create Fibbonaci series upto entered term
n=int(input("Enter Number:"))
a,b=0,1
print(a)
for i in range(n):
    a,b=b,a+b
    print(a)



