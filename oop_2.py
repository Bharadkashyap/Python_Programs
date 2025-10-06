#28-02-2024

#Polymophism
class Bca:
    def student(self):
        print("total student=300")
class Bscit:
    def student(self):
        print("total student=120")
        
b=Bca()
b.student()
i=Bscit()
i.student()
#polymorphishm with inheritance
#method overridding & super function
class Man:
    def qualities(self):
        print("good listener")
        print("care\nlove")
    def field(self):
        print("Work is must")
class Student(Man):
    def field(self):
        super().field()
        print("In IIT")
class Father(Man):
    def field(self):
        print("In MBA")
f1=Father()
f1.qualities()
f1.field()
print("-----------")
s1=Student()
s1.qualities()
s1.field()

#function with default arguments
#1.....
def Wish(str="good day"):
    print("hi.....",str)
Wish()
Wish("good morning")
#2......
def val(a,b=20):
    print(a)
    print(b)
val(10)
val(10,20)
#function with keyword arguments
def val(a,b=500):
    print(a)
    print(b)
val(10)
val(10,20)
val(a=100,b=200)
val(b=110,a=220)

#function with required argument
def val(a,b):
    print(a,b)
val(10,20)
#val(10)error

#function with return value
def val(a,b):
    print(a)
    print(b)
    s=a+b
    print(s)
val(10,20)

#function with multiple return  values
def val(a,b):
    a=a+5
    b=b+10
    return a,b
x,y=val(5,20)
print(x,"\n",y)
print("-------")
#Variealble -Length Argument
def val(*numbers):
    for i in numbers:
        print(i)
x=val(10,20,30,40,50,60,70,80,90,100)



