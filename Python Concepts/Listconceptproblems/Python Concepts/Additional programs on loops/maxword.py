line=input("enter line of text:")
if(len(line)==0):
    print("no text")
else:
    if(line.isspace()):
        print("no text")
    else:
        dw={} #create an empty dict for placing word
        words=line.split()
        for word in words:
            dw[word]=len(word)
        else:
            vals=dw.values()
            for word,wordlen in dw.items():
                if(wordlen==max(vals)):
                    print("{}".format(word))