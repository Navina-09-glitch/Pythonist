with open("hyd.info","a") as fp:
    print("enter information and press(@ to stop):")
    while(True):
        kbdata=input()
        if(kbdata!="@"):
            fp.write(kbdata+"\n")
        else:
            break