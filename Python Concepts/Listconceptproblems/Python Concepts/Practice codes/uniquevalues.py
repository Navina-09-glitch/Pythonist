s="MISSISSIPPI"
st=set(s)
print(st)
uv=list()
for val in s:
    if val not in uv:
        uv.append(val)
print(uv)
