s="PYTHON"
print(s[0:4])
for ch in s:
    print(ch)
else:
    print ("Iam from else part of for loop")
#By using loop with break#
for ch in s:
    if (ch=="O"):
        break
    print(ch,end="")
else:
    print("I'm from else")
print()
print("other statements in program")