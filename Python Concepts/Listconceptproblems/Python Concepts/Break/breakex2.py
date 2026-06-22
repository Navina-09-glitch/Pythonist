s="PYTHON"
print(s[0:4])
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("Iam from else part of while loop")
#My Requirement is to display only "PYTH" with out using slicing and indexing
print("By using while loop with break")
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i=i+1
else:
    print("Iam from else part of while loop")
print()
print("Other statements in program")