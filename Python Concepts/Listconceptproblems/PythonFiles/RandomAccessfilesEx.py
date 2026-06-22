#Priogram for Demonstrating Random Access file
#tell() gives Index of File pointer
#seek() will reset the File pointer to Specified Valid Index to File Data
#RandomAccessFileEx.py
with open("hyd.info","r") as fp:
    print("Initial Index pointed by fp=",fp.tell()) # 0
    randata=fp.read(3)
    print("random Data=",randata) # HYD
    print("Index pointed by fp=", fp.tell())  # 3
    randata = fp.read(8)
    print("random Data=", randata) #  is the
    print("Index pointed by fp=", fp.tell())  # 11
    randata = fp.read(7)
    print("random Data=", randata)  #capital
    print("Index pointed by fp=", fp.tell())  # 18
    print("-----------------------------------------")
    randata = fp.read()
    print("random Data=", randata)  #
    print("Index pointed by fp=", fp.tell())  #
    print("-----------------------------------------")
    randata = fp.read()
    print("random Data=", randata)  #
    print("Index pointed by fp=", fp.tell())  #
    print("-----------------------------------------")
    #reset the file pointer Index to 11 Index
    fp.seek(11)
    print("Index pointed by fp=", fp.tell())  #11
    randata = fp.read(7)
    print("random Data=", randata)  # capital
    print("Index pointed by fp=", fp.tell())  # 18
    print("-----------------------------------------")
    # reset the file pointer Index to 0 th Index
    fp.seek(0)
    randata = fp.read(18)
    print("random Data=", randata)  #
    print("Index pointed by fp=", fp.tell())  # 18
    print("-----------------------------------------")