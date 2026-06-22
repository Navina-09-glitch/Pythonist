correctpassword='admin123'
attempts=0
Maxattempts=3
#0<3
#1<3
#2<3
#3<3
while attempts<Maxattempts:
    password=input("Please enter your password: ")
    if password== correctpassword:
        print("Password is correct")
    else:
        attempts+=1
