#Result of 4 subject
name=input("Enter student name:")
rollno=int(input("Enter rollno:"))
sub1=int(input("Enter Java marks:"))
sub2=int(input("Enter Python marks:"))
sub3=int(input("Enter PHP marks:"))
sub4=int(input("Enter Android marks:"))
#calculation 
tot=sub1+sub2+sub3+sub4
per=tot/4

print("Name is:",name)
print("rollno is:",rollno)
#condition for grading system

if per>=90 and per<=100:
           print("Grade O with ",per,"%")
elif per>=80 and per<90:
           print("Grade A+ with ",per,"%")
elif per>=70 and per<80:
           print("Grade A with ",per,"%")
elif per>=60 and per<70:
           print("Grade B with ",per,"%")
elif per>=40 and per<60:
           print("Grade C with ",per,"%")
elif per>=35 and per<40:
           print("Grade F with ",per,"%")
else :
     print("Grade Fail with ",per,"%")
