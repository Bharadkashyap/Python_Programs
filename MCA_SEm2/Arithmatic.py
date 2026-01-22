#Arithmatic operation

no1=float(input("Enter first number"))
no2=float(input("Enter Second number"))
ch=input("Enter choice:+,-,*,/")

#match case
match(ch):
    case '+':   #case1 addition
        add=no1+no2
        print("addtion is:",add)
    case '-': #case2 substration
        sub=no1-no2
        print("substraction is:",sub)
    case '*': #case3 multiplication
        mul=no1*no2
        print("multiplication is:",mul)
    case '/': #case4 division
        div=no1/no2
        print("division is:",div)
    case _:
        print("invalid choice")
