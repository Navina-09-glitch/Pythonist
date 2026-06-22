while(True):
    eno=int(input("enter no:"))
    empname=input("Enter your name:")
    sal=float(input("Enter your salary:"))
    with open("emp.data","a") as fp:
        fp.write(str(eno)+"\t")
        fp.write(empname+"\t")
        fp.write(str(sal)+"\n")
        print("Data written to the file--verify")
        print("-"*50)
        ch=input("Do you want to insert another record(yes/no):")
        if(ch.lower()=="no"):
            print("Thnx for using this program")
            break
