lst=[]
for i in range(1,4):
    layer=[]
    for r in range(1,5):
        row=[]
        for c in range(1,7):
            row.append('*')
        layer.append(row)
    lst.append(layer)
for i in range(1,4):
    print("layer",i)
    for row in lst[i-1]:
        print(row)
    print()