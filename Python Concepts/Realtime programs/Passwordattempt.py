attempts=0
while attempts < 5:
    pwd=input("Enter password: ")
    if pwd=="secret":
        print("access granted")
        break
    attempts+=1
else:
    print("Too many failed attempts, access denied.")