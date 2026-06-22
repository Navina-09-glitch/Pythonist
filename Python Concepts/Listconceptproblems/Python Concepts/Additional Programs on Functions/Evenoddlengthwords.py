def findwordlength(word):
    if (len(line)==0):
        print("Enter line of text with words")
    elif(line.isspace()):
        print("Enter line of text with words not an empty string")
    else:
        odddict={}
        evendict={}
        words=word.split()
        for word in words:
            if(len(word)%2==0):
                evendict[word]=len(word)
            else:
                odddict[word]=len(word)
        else:
            print("even words and their length")
            for w,l in evendict.items():
                print("\t {}-->{}".format(w,l))
            print("odd words and their length")
            for w,l in odddict.items():
                print("\t {}-->{}".format(w,l))
            for wl in evendict.items():
                print("\t {}-->{}".format(wl[0],wl[1]))
            for x in odddict.items():
                print("\t {}-->{}".format(x,odddict.get(x)))
line=input("Enter line of text: ")
findwordlength(line)
