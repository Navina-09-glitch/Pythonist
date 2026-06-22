#Program for getting Value as key and key as value from Dict
#Given input: d={"Python":10,20:"C",30:"Java",40:"Django"}
#Expected output: d1={"Python":10,"C":20,"Java":30,"Django":40}

d={10:"Python",20:"C",30:"Java",40:"Django"}
d1={value:key for key,value in d.items()}
print("original dictionary")
print(d)
print("Reversed dictionary")
print(d1)

#Below approach is without using dict comprehension
rd={}
for k,v in d.items():
    rd[v]=k
else:
    print("Original Dict")
    print(d)
    print("Reversed Dict")
    print(rd)
#Below approach is without using items
#d[k] will give the value that will become key
revdict={}
for k in d:
    revdict[d[k]]=k
else:
    print("Original Dict")
    print(d)
    print("Reversed Dict")
    print(revdict)
rev_dict={}
for k in d:
    rev_dict[d.get(k)]=k
else:
    print("Original Dict")
    print(d)
    print("Reversed Dict")
    print(rev_dict)