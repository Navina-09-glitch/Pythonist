s="PYTHON"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("Iam from else part of for loop")
for ch in s:
    if ch in ["T","O"]:
         continue
    print(ch,end="")
else:
    print("Iam from else part of for loop")
