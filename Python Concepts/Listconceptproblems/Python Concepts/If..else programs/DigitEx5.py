d1={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",
    -1:"-One",-2:"-Two",-3:"-Three",-4:"Four",-5:"-Five",-6:"-Six",-7:"-Seven",-8:"-Eight",-9:"-Nine"}
dig=int(input("Enter a number: "))
print("{} is {}".format(dig,d1[dig]) if d1.get(dig)!=None else "positive number" if dig>9 else "negative number")


#d1={0:"Zero",1:"one",2:"two",3:"Three",4:"Four",5:"Five",6:"Six",7:"seven",8:"Eight",9:"Nine",-1:"-one",-2:"-two",-3:"-Three",-4:"-Four",-5:"-Five",-6:"-Six",-7:"-seven",-8:"-Eight",-9:"-Nine"}
digit=int(input("enter number"))
#if d1.get(digit)!=None:
    #print("{} is {}".format(digit,d1[digit]))
#else:
    #if digit>9:
        #print("positive number")
    #else:
       #print("Negative number")#