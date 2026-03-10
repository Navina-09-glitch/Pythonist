n=int(input("enter no of words"))
if (n<=0):
    print("input is invalid".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=input("enter {}th word".format(i))  #here datatype is string
        lst.append(val)
    else:
        print(lst)
        longer_words=[]
        x=int(input("minimum length of word:"))
        for k in lst:
            if len(k)>x:
                longer_words.append(k)
        print("words longer than n",longer_words)



