#My requirement is to display pyhon using while loop
s="python"
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("Iam from else part of while loop")
i=0
while(i<len(s)):
    if(s[i]=="t"):
        i=i+1
        continue
    print(s[i],end="")
    i=i+1
else:
    print("Iam from else part of program")
