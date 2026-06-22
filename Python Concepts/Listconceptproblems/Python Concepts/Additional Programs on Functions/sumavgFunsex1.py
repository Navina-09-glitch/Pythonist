def readvalues():
    nov=int(input("Enter number of values you have:"))
    if(nov<=0):
        return []
    else:
        lst=[]
        for i in range(1,nov+1):
            val=float(input("Enter value for {}:".format(i)))
            lst.append(val)
        return lst
def findsumavg(lst):
    if(len(lst)==0):
        print("list is empty----can't find sum and average")
    else:
        s=0
        for val in lst:
            print("\t {}".format(val))
            s=s+val
        else:
            print("sum={}".format(s))
            print("avg={}".format(s/len(lst)))
#Main Program
lst=readvalues()
findsumavg(lst)