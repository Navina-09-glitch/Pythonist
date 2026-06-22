import csv
with open ("E:\\KVR-PYTHON-11AM\\CSV\\emp.csv") as fp:
    csvdr=csv.DictReader(fp)
    for row in csvdr:
        for k,v in row.items():
            print("{}-->{}".format(k,v))
        print("-"*50)
