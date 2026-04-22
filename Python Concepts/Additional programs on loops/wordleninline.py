line=input("enter line :")
if(len(line)==0):
    print("enter a line of text:")
else:
    if(line.isspace()):
        print("dont enter space")
    else:
        dw={}
        words=line.split()
        print("given line {}=".format(line))
        for word in words:
            dw[word]=len(word)
        else:
            for w,wl in dw.items():
                print("\t\t {}-->{}".format(w,wl))