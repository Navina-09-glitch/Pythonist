#Program for counting Number of Lines, words and Chars
#I have written two lines of data in stud1.data file
#nl=number of lines,nw=number of words,nc=number of characters
nl,nw,nc=0,0,0
filename=input("Enter the file name for counting number of lines,words and chars") #when asked in compiled , I tried with stud1.data,hyd.info
with open(filename,"r") as fp:
    lines=fp.readlines()
    for line in lines:
        nl=nl+1
        nw=nw+len(line.split())
        nc=nc+len(line)
    else:
        print("Number of lines",nl)
        print("Number of words",nw)
        print("Number of characters",nc)