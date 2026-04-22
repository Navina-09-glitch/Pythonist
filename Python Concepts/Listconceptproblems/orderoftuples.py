from operator import itemgetter
def sort_by_last(tuples):
    return sorted(tuples,key=itemgetter(-1))
sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
result=sort_by_last(sample_list)
print("sorted list:",result)