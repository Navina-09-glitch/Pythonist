#Program for adding new Record to the CSV File
import csv
records=[780,"RAN",5.3,"Teacher"]
with open("E:\\KVR-PYTHON-11AM\\CSV\\emp.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(records)
    print("Records added to CSV File-----Verify")