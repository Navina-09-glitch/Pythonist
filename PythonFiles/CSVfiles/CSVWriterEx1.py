#Program for Creating the CSV File with inner List
#CSVWriterEx1.py
import csv #Step-1
hnames=["EMPNO","NAMES","SAL","DSG"] #Step-2
records=[[100,"RS",4.5,"Author"],
         [200,"DR",6.6,"Doctor"],
         [300,"SS",1.5,"Actor"],
         [400,"ST",4.5,"SE"],
         [500,"SQ",8.5,"PM"]] #Step-3
with open ("E:\\KVR-PYTHON-11AM\\CSV\\emp.csv",'a') as fp: #Step-4
     csvwr= csv.writer(fp) #step-5
     #write the header names to file---step-6
     csvwr.writerow(hnames)
     #write records to the file---inner list---step-7
     csvwr.writerows(records)
     print("CSV file created--------Verify")

