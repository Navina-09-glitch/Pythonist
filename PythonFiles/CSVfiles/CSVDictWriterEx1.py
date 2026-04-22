#program for Creating CSV File Dict Data
import csv
hn=["PID","NAME","PRICE"]
records=[{"PID":100,"NAME":"Cadburry","PRICE":120.45},
        {"PID":200,"NAME":"Almond","PRICE":85.45},
        {"PID":300,"NAME":"KitKat","PRICE":20.45},
        {"PID":400,"NAME":"ChockPie","PRICE":100.25},
        {"PID":500,"NAME":"kinderJoy","PRICE":50.45}]
with open("E:\\KVR-PYTHON-11AM\\CSV\\sales.csv","w") as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=hn)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File Created with Dict Data--verify")