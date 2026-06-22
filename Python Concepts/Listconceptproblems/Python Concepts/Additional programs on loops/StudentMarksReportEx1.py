#Student Number Validation
while(True):
    sno=input("enter student number:")
    if sno.isdigit() and int(sno) in range(100,201):
        break
    else:
        print("invalid student number".format(sno))
#student name validation
while(True):
    name=input("enter student name:")
    words=name.split()
    nv=True
    for word in words:
            if not word.isalpha():
                nv=False
                break
    if nv:
        break
    else:
        print("invalid student name".format(name))
#Validation of C Lang Marks-- 0 to 100
while(True):
    cm=input("enter c lang marks (0-100):")
    if (cm.isdigit()) and (0<int(cm)<=100):
        break
    else:
        print("{} is invalid c lang marks".format(cm))
#Validation of CPPM Lang Marks-- 0 to 100
while(True):
    cppm=input("enter cppm lang marks (0-100):")
    if (cppm.isdigit()) and (0<int(cppm)<=100):
        break
    else:
        print("{} is invalid cppm lang marks".format(cppm))
#Validation of Python Lang Marks-- 0 to 100
while(True):
    python=input("enter python lang marks (0-100):")
    if (python.isdigit()) and (0<int(python)<=100):
        break
    else:
        print("{} is invalid python lang marks".format(python))
#Calculate Total marks and Percentage of marks

totmarks=int(cm)+int(cppm)+int(python)
percent=(totmarks/300)*100

#Decide the Grade
if int(cm) < 40 or int(cppm) < 40 or int(python) < 40:
    grade = "FAIL"
else:
    if percent >= 75:
        grade = "DISTINCTION"
    elif percent >= 60:
        grade = "FIRST"
    elif percent >= 50:
        grade = "SECOND"
    elif percent >= 40:
        grade = "THIRD"
    else:
        grade = "NO GRADE"  # fallback to avoid NameError


#display the student marks report
print("\t\t STUDENTS MARKS REPORT")
print("\t\t Student Number:{}".format(sno))
print("\t\t Student name:{}".format(name))
print("\t\t Student C marks:{}".format(cm))
print("\t\t Student C++ marks:{}".format(cppm))
print("\t\t Student Python marks:{}".format(python))
print("\t\t Student total marks:{}".format(totmarks))
print("\t\t Student percentage of marks {}%".format(percent))
print("\t\t Student Grade: {}".format(grade))