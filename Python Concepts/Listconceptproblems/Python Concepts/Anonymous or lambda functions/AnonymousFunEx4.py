def readvalues():
    nov=int(input("Enter how many values you have"))
    if(nov<=0):
        return []
    else:
        lst=[]
        for i in range(1,nov+1):
            val=float(input("Enter {} value:".format(i)))
            lst.append(val)
        else:
            return lst
#Anonymous Function Def

findmax=lambda lst:max(lst)
findmin=lambda lst:min(lst)

#Main program
lst=readvalues()
if(len(lst)==0):
    print("List is empty--can't find max and min")
else:
    maxval=findmax(lst)
    minval=findmin(lst)
    print("Max value is {}".format(lst, maxval))
    print("Min value is {}".format(lst, minval))
