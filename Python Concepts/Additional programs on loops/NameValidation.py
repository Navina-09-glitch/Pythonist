name=input("enter your name")
print("given name {}".format(name))
words=name.split()
nv=True
for word in words:
    if (not word.isalpha()):
        nv=False
        break
if (nv):
    print("{} is valid".format(name))
else:
    print("{} is invalid".format(name))