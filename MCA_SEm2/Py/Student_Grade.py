#Grade Of student
nm=input("Enter Name:")
per=int(input("Enter Percentage:"))
print(f"{nm} is a name of student")

if per>=90:
        print(f"{per}Distriction O Grade")
elif per>=70 and per<90:
    print(f"{per} First Class with A+")
elif per>=50 and per<70:
    print(f"{per} First Class with A")
elif per>=40 and per<50:
    print(f"{per} Second Class with B")
elif  per<40:
    print(f"{per} Failed ")
else:
    print("invalid input")
    
    
    
        
