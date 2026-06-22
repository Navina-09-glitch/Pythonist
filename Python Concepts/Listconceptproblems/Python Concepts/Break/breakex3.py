s="MISSISSIPPI"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("Iam from else part of for loop")
#My requirement is to display only "MISS" with out using indexing and slicing
ctr=0
for ch in s:
    if(ch=="I"):
        ctr+=1
        if(ctr==2):
            break
    print(ch,end="")
else:
    print("I'm from else part of for loop")
print("\nother statements in program")