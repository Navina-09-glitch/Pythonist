import csv
noc=int(input("Enter how many columns you have: "))
if(noc<=0):
    print("Please enter a valid number of columns".format(noc))
else:
    colnames=[]
    for i in range(1,noc+1):
        colname=input("Enter column name {}: ".format(i))
        colnames.append(colname)
    else:
        nor=int(input("Enter how many rows/records you have: "))
        if(nor<=0):
            print("Please enter a valid number of rows/records".format(nor))
        else:
            records=list()
            for rno in range(1,nor+1):
                val=input("Enter {} record details: ".format(rno))
                record=[]
                for recno in range(0,len(colnames)):
                    val=input("Enter {} record details: ".format(colnames[recno]))
                    record.append(val)
                records.append(record)
            else:
        # [['1000', 'Rossum'], ['2000', 'Travis'], ['3000', 'KVR']]
                 while(True):
                     filename=input("Enter CSV file name with extension .csv: ")
                     if(filename.endswith(".csv")):
                         with open("E:\\KVR-PYTHON-11AM\\CSV\\" + str(filename), "a") as fp:
                             csvwr = csv.writer(fp)
                             csvwr.writerow(colnames)
                             csvwr.writerows(records)
                             print("CSV File Created Dynamically--verify")
                             break
                     else:
                         print("\tInvalid CSV File Extension--try again")


