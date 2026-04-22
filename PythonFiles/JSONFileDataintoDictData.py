#JSONFileDataIntoDictData.py
import json
try:
    with open("E:\\KVR-PYTHON-11AM\\JSON\\studjson.json","r") as fp:
        record=json.load(fp)
        print("-----------------------------------------")
        for key,value in record.items():
            print("{}-->{}".format(key,value))
        print("-----------------------------------------")
except FileNotFoundError:
    print("Json File Does not Exist")