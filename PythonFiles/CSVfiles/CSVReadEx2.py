import csv
with open("E:\\KVR-PYTHON-11AM\\CSV\\emp.csv","r") as fp:
    csvr=csv.reader(fp) # csvr is an object of <class, _csv.reader>
    print(csvr,type(csvr))
    for record in csvr:
        print(record,type(record))
        for val in record:
            #print(val,type(val))
            print("{}".format(val),end="\t\t")
        print()
    print("-"*50)