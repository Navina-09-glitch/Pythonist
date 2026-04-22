n=int(input("enter a number"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    s=0
    ss=0
    cs=0
    for i in range(1,n+1):
        print("\t{}\t\t\t\t {}\t\t\t\t {}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("\t\t{} \t\t\t\t {} \t\t\t\t {}".format(s,ss,cs))