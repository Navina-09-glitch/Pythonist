shallow_list=[[1,2],[3,4],[5,6]]
flat_list=[]
for sublist in shallow_list:
    for item in sublist:
        flat_list.append(item)
print("original list:{}",shallow_list)
print("flattened list:{}",flat_list)