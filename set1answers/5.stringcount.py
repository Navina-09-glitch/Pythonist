def match_count(strings):
    count=0
    for s in strings:
        if len(s)>=2 and s[0] ==s[-1]:
            count+=1
    return count
sample_list=['abc','xyz','aba','1221']
result= match_count(sample_list)
print("result:",result)