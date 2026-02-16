"""list1=[10,20]
print("List is:",list1)
list1.append(100)#Add Element
print("Add new Element:",list1)
list1.remove(10)# Remove element
print("After removing:",list1)
list1[1]=30 #change the value 

print("Final List is :",list1) #Display final value"""
lit=[]

while True:
    print("-----Menu -----\n1.Add ELement \n2.Delete Element\n3.Display List\n4.sort list\n5.search Element\n6.exit")
    ch=int(input("Enter choice:"))
    if ch == 1:
        it=int(input("Enter Element"))
        lit.append(it)
    elif ch == 2:
        it=int(input("Enter delete element"))
        if it in lit:
            lit.remove(it)
            print("Deleted")
        else:
            print("not found")
    elif ch == 3:
        print("Current List:", lit)
    elif ch == 4:
        lit.sort()
        print("Sorted List:", lit)
    elif ch == 5:
        it = int(input("Enter element to search: "))
        if it in lit:
            print("found at index:", lit.index(it))
        else:
            print("Element not found.")
    elif ch == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
        
