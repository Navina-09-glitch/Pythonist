import json
d={"SNO":100,"NAME":"Rossum","Marks":45.67}
print("Dict data")
print("\t{}\t{}".format(d,type(d)))
#Save dict data into JSON File as Record ---we use dump()
with open("E:\\KVR-PYTHON-11AM\\JSON\\studjson.json",'w') as fp:
    json.dump(d,fp)
    print("Dict data saved as record in file--verify")