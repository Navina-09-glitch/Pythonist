d={"Python":10,20:"C",30:"Java",40:"Django"}
d1={}
for k,v in d.items():
    d1[v]=k
print("Original dictionary:",d)
print("Swapped dictionary:",d1)