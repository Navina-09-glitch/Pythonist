d=int(input("enter number"))
if(d==0):
    print("{} is zero".format(d))
else:
    if(d==1):
        print("{} is one".format(d))
    else:
        if(d==2):
            print("{} is two".format(d))
        else:
            if(d==3):
                print("{} is three".format(d))
            else:
                if(d==4):
                    print("{} is four".format(d))
                else:
                    if(d==5):
                        print("{} is five".format(d))
                    else:
                          if(d==6):
                            print("{} is six".format(d))
                          else:
                              if(d==7):
                                print("{} is seven".format(d))
                              else:
                                  if(d==8):
                                    print("{} is eight".format(d))
                                  else:
                                    if(d==9):
                                        print("{} is nine".format(d))
                                    else:
                                        if(d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
                                            print("{} is negative digit".format(d))
                                        else:
                                            if(d>9):
                                                print("{} is positive digit".format(d))
                                            else:
                                                print("{} is negative digit".format(d))
print("Program executed completed")
