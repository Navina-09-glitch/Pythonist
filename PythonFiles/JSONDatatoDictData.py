import json
jsondata='{"SNO":"100","NAME":"Rossum","Marks":"77.99"}' #the JSON object must be str, bytes or bytearray, not dict
print("JSON data")
print("\t{}\t{}".format(jsondata,type(jsondata)))
#convert JSON data into Dict data-- --we use loads() of json module
d=json.loads(jsondata)
print("dict data")
print("\t{}\t{}".format(d,type(d)))
for key,value in d.items():
    print("\t{}\t{}".format(key,value))

#Use json.loads() when you have a JSON string and want a Python dict.
#Use json.dumps() when you have a Python dict and want a JSON string.
#here if you notice carefully i have given single quotes ''